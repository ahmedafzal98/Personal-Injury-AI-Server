import React from "react";

const Skeleton = () => (
  <div className="animate-pulse space-y-3">
    <div className="h-4 bg-indigo-100 rounded w-3/4"></div>
    <div className="h-4 bg-indigo-100 rounded w-5/6"></div>
    <div className="h-4 bg-indigo-100 rounded w-2/3"></div>
    <div className="h-4 bg-indigo-100 rounded w-full"></div>
    <div className="h-4 bg-indigo-100 rounded w-4/5"></div>
  </div>
);

export default Skeleton;
