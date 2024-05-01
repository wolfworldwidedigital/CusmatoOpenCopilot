import type { Options } from "@lib/types";
import type { ReactNode } from "react";
import { createSafeContext } from "./createSafeContext";

export type ConfigDataContextType = Omit<
  Options,
  "containerProps" | "triggerSelector"
>;

const [useConfigData, ConfigDataSafeProvider] =
  createSafeContext<ConfigDataContextType>();

export function ConfigDataProvider({
  children,
  data,
}: {
  data: ConfigDataContextType;
  children: ReactNode;
}) {
  return (
    <ConfigDataSafeProvider
      value={{
        debug: data.debug ?? false,
        ...data,
      }}
    >
      {children}
    </ConfigDataSafeProvider>
  );
}

// eslint-disable-next-line react-refresh/only-export-components
export { useConfigData };
