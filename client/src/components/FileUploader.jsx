import React, { useState } from "react";
import { motion } from "framer-motion";
import { Upload, Loader2 } from "lucide-react";

const FileUploader = ({
  setData,
  setLoading,
  setSummary,
  setError,
  loading,
  data,
  error,
}) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError("");
    setData(null);
    setSummary("");
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a file first.");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "https://personal-injury-ai-server-hlj8.onrender.com/extract",
        {
          method: "POST",
          body: formData,
        }
      );

      const result = await response.json();
      if (result.error) throw new Error(result.error);
      setData(result);

      console.log(result);

      // Simulated AI summary
      setTimeout(() => {
        setSummary(
          "Once the OpenAI API is integrated, the AI will provide a clear 10-point summary of your document."
        );
      }, 2000);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2 className="text-lg font-semibold text-indigo-600 mb-4">
        Upload a Document
      </h2>

      {/* Upload Box */}
      <div className="border-2 border-dashed border-indigo-300 rounded-xl p-6 text-center bg-white/60 hover:bg-indigo-50 transition cursor-pointer">
        <input
          type="file"
          onChange={handleFileChange}
          accept=".pdf,.docx,.jpg,.jpeg,.png"
          className="hidden"
          id="file-upload"
        />
        <label htmlFor="file-upload" className="cursor-pointer">
          <Upload size={40} className="mx-auto text-indigo-500 mb-2" />
          <span className="text-indigo-700 font-medium">
            Click to upload or drag a file
          </span>
          {file && <p className="mt-2 text-gray-500 text-sm">{file.name}</p>}
        </label>
      </div>

      {/* Upload Button */}
      <motion.button
        whileHover={{ scale: 1.03 }}
        whileTap={{ scale: 0.97 }}
        onClick={handleUpload}
        disabled={loading}
        className="mt-6 w-full bg-indigo-600 text-white font-semibold py-2.5 rounded-lg hover:bg-indigo-700 shadow-lg transition"
      >
        {loading ? (
          <span className="flex items-center justify-center gap-2">
            <Loader2 size={20} className="animate-spin" /> Extracting...
          </span>
        ) : (
          "Upload & Extract"
        )}
      </motion.button>

      {/* Error / Success */}
      {error && (
        <p className="text-red-500 text-sm mt-4 bg-red-50 p-2 rounded-md border border-red-200">
          ⚠️ {error}
        </p>
      )}
      {data && (
        <div className="mt-6 bg-green-50 border border-green-200 p-3 rounded-md text-sm text-green-700">
          ✅ Extraction Complete <br />
          <strong>Filename:</strong> {data.filename}
          <br />
          <strong>Characters:</strong> {data.text_length}
        </div>
      )}
    </div>
  );
};

export default FileUploader;
