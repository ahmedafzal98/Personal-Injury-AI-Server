import React from "react";
import { Sparkles } from "lucide-react";
import Skeleton from "./Skeleton";

const AISummary = ({ summary, loading }) => {
  return (
    <div>
      <h2 className="text-lg font-semibold text-indigo-600 mt-8 mb-3 flex items-center gap-2">
        <Sparkles className="text-indigo-500" size={20} /> AI Summary
      </h2>
      <div className="bg-gradient-to-br from-indigo-50 via-white to-indigo-100 border border-indigo-100 rounded-xl p-4 shadow-inner h-[25vh] overflow-y-scroll text-sm text-gray-700 whitespace-pre-line">
        {loading ? (
          <Skeleton />
        ) : summary ? (
          summary
        ) : (
          <p className="text-gray-400 text-center mt-6">
            AI summary will appear here after extraction ✨
          </p>
        )}
      </div>
    </div>
  );
};

export default AISummary;
