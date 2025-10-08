import React, { useState } from "react";
import { motion } from "framer-motion";
import Header from "./layout/Header";
import Footer from "./layout/Footer";
import FileUploader from "./components/FileUploader";
import ExtractedText from "./components/ExtractedText";
import AISummary from "./components/AISummary";

const App = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-br from-indigo-50 via-white to-indigo-100 font-sans">
      <Header />

      <div className="flex flex-col md:flex-row flex-grow">
        {/* Left Panel */}
        <motion.div
          initial={{ x: -50, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ duration: 0.6 }}
          className="md:w-1/3 w-full p-6 border-r border-indigo-100 bg-white/80 backdrop-blur-xl"
        >
          <FileUploader
            setData={setData}
            setLoading={setLoading}
            setSummary={setSummary}
            setError={setError}
            loading={loading}
            data={data}
            error={error}
          />
        </motion.div>

        {/* Right Panel */}
        <motion.div
          initial={{ x: 50, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ duration: 0.6 }}
          className="flex-grow p-6 overflow-y-auto"
        >
          <ExtractedText data={data} loading={loading} />
          <AISummary summary={summary} loading={loading} />
        </motion.div>
      </div>

      <Footer />
    </div>
  );
};

export default App;
