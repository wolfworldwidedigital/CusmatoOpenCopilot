import { createRoot } from "react-dom/client";
import type { Options as BaseOptions } from "../lib/types";
import Root from "../lib/Root";
import { CopilotWidget } from "../lib/CopilotWidget";
import { composeRoot } from "./utils";

const defaultRootId = "opencopilot-root";
interface Options extends Omit<BaseOptions, "components"> {
  rootId?: string;
}
declare global {
  interface Window {
    initAiCoPilot: typeof initAiCoPilot;
  }
}

/**
 * @param rootId The id of the root element for more control, you don't need to use this unless you want more control over the widget
 * @description Initialize the widget
 */
function initAiCoPilot({
  triggerSelector,
  containerProps,
  rootId,
  ...options
}: Options) {
  const container = composeRoot(rootId ?? defaultRootId, rootId === undefined);
  createRoot(container).render(
    <Root
      options={{
        ...options,
      }}
      containerProps={containerProps}
    >
      <CopilotWidget triggerSelector={triggerSelector} __isEmbedded />
    </Root>
  );
}

window.initAiCoPilot = initAiCoPilot;
