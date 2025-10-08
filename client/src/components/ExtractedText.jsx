import React from "react";
import Skeleton from "./Skeleton";

const ExtractedText = ({ data, loading }) => {
  return (
    <div>
      <h2 className="text-lg font-semibold text-indigo-600 mb-3">
        Extracted Text
      </h2>
      <div className="bg-white/80 backdrop-blur-xl border border-indigo-100 rounded-xl p-4 shadow-glow h-[60vh] overflow-y-scroll text-sm text-gray-700 whitespace-pre-line">
        {loading ? (
          <Skeleton />
        ) : data ? (
          data.extracted_text
        ) : (
          <p className="text-gray-400 text-center mt-10">
            Upload a file to view extracted text here.
          </p>
        )}
      </div>
    </div>
  );
};

export default ExtractedText;
