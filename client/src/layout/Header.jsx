import React from "react";
import { FileText } from "lucide-react";

const Header = () => (
  <header className="px-6 py-4 shadow-md bg-white/70 backdrop-blur-lg border-b border-indigo-100">
    <h1 className="text-2xl font-bold text-indigo-700 tracking-wide flex items-center gap-2">
      <FileText className="text-indigo-500" size={24} />
      Document Extractor AI
    </h1>
  </header>
);

export default Header;
