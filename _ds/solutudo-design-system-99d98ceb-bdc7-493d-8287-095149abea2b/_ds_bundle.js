/* @ds-bundle: {"format":3,"namespace":"SolutudoDesignSystem_99d98c","components":[{"name":"Button","sourcePath":"components/buttons/Button.jsx"},{"name":"Avatar","sourcePath":"components/display/Avatar.jsx"},{"name":"Badge","sourcePath":"components/display/Badge.jsx"},{"name":"Card","sourcePath":"components/display/Card.jsx"},{"name":"StatTile","sourcePath":"components/display/StatTile.jsx"},{"name":"Input","sourcePath":"components/forms/Input.jsx"},{"name":"SearchBar","sourcePath":"components/forms/SearchBar.jsx"},{"name":"SegmentedToggle","sourcePath":"components/forms/SegmentedToggle.jsx"},{"name":"FeedItem","sourcePath":"components/marketing/FeedItem.jsx"},{"name":"PlanCard","sourcePath":"components/marketing/PlanCard.jsx"}],"sourceHashes":{"components/buttons/Button.jsx":"ee110446b757","components/display/Avatar.jsx":"a089413e44ac","components/display/Badge.jsx":"27cb2db9f47d","components/display/Card.jsx":"a030fc45c62e","components/display/StatTile.jsx":"9cfebe6429c0","components/forms/Input.jsx":"eb936f3ff05b","components/forms/SearchBar.jsx":"56922c449a88","components/forms/SegmentedToggle.jsx":"d5aa9b2675b2","components/marketing/FeedItem.jsx":"ca211684759c","components/marketing/PlanCard.jsx":"9393b0315822","ui_kits/business/app.jsx":"afa265c2de0b","ui_kits/business/dashboard.jsx":"8bb23d5749d7","ui_kits/business/landing.jsx":"692837d17014","ui_kits/business/plancard.jsx":"f1c33f02f86a","ui_kits/consumer-search/app.jsx":"d158e6655a1b","ui_kits/consumer-search/movimento.jsx":"1831b08ea1ce","ui_kits/consumer-search/screens.jsx":"5c8852f97404","ui_kits/shared/icons.jsx":"8b425b095612","ui_kits/shared/primitives.jsx":"998245822878"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.SolutudoDesignSystem_99d98c = window.SolutudoDesignSystem_99d98c || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/buttons/Button.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Solutudo Button — pill-shaped action with the brand's variant set.
 * Styling reads design-system CSS custom properties (no CSS-in-JS lib).
 */
function Button({
  children,
  variant = "primary",
  // primary | dark | secondary | ghost | whatsapp
  size = "md",
  // sm | md | lg
  iconLeft = null,
  iconRight = null,
  fullWidth = false,
  disabled = false,
  onClick,
  style = {},
  ...rest
}) {
  const sizes = {
    sm: {
      fontSize: 13,
      padding: "9px 16px",
      gap: 7,
      icon: 16
    },
    md: {
      fontSize: 15,
      padding: "13px 24px",
      gap: 9,
      icon: 18
    },
    lg: {
      fontSize: 17,
      padding: "17px 32px",
      gap: 10,
      icon: 20
    }
  };
  const s = sizes[size] || sizes.md;
  const base = {
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    gap: s.gap,
    fontFamily: "var(--font-sans)",
    fontWeight: 600,
    fontSize: s.fontSize,
    letterSpacing: "var(--tracking-snug)",
    padding: s.padding,
    border: "none",
    borderRadius: "var(--radius-pill)",
    cursor: disabled ? "not-allowed" : "pointer",
    width: fullWidth ? "100%" : "auto",
    whiteSpace: "nowrap",
    transition: "transform var(--dur-fast) var(--ease-out), box-shadow var(--dur-base) var(--ease-out), filter var(--dur-base) var(--ease-out)",
    opacity: disabled ? 0.45 : 1,
    lineHeight: 1
  };
  const variants = {
    primary: {
      background: "var(--grad-cta)",
      color: "var(--white)",
      boxShadow: "var(--shadow-brand)"
    },
    dark: {
      background: "var(--ink)",
      color: "var(--white)"
    },
    secondary: {
      background: "var(--white)",
      color: "var(--ink)",
      boxShadow: "var(--ring-hairline)"
    },
    ghost: {
      background: "transparent",
      color: "var(--brand-purple)"
    },
    whatsapp: {
      background: "#25D366",
      color: "var(--white)"
    }
  };
  const onEnter = e => {
    if (disabled) return;
    e.currentTarget.style.transform = "translateY(-1px)";
    if (variant === "primary") e.currentTarget.style.filter = "brightness(1.05)";
    if (variant === "dark") e.currentTarget.style.filter = "brightness(1.25)";
    if (variant === "secondary") e.currentTarget.style.boxShadow = "var(--shadow-sm), var(--ring-hairline)";
  };
  const onLeave = e => {
    e.currentTarget.style.transform = "none";
    e.currentTarget.style.filter = "none";
    if (variant === "secondary") e.currentTarget.style.boxShadow = "var(--ring-hairline)";
  };
  const onDown = e => {
    if (!disabled) e.currentTarget.style.transform = "scale(0.97)";
  };
  const onUp = e => {
    if (!disabled) e.currentTarget.style.transform = "translateY(-1px)";
  };
  return /*#__PURE__*/React.createElement("button", _extends({
    type: "button",
    disabled: disabled,
    onClick: onClick,
    onMouseEnter: onEnter,
    onMouseLeave: onLeave,
    onMouseDown: onDown,
    onMouseUp: onUp,
    style: {
      ...base,
      ...variants[variant],
      ...style
    }
  }, rest), iconLeft && /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      width: s.icon,
      height: s.icon
    }
  }, iconLeft), children, iconRight && /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      width: s.icon,
      height: s.icon
    }
  }, iconRight));
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/buttons/Button.jsx", error: String((e && e.message) || e) }); }

// components/display/Avatar.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Avatar — circular user/business image with optional gradient ring.
 * Falls back to an initial on a tinted background.
 */
function Avatar({
  src = null,
  name = "",
  size = 48,
  ring = false,
  // false | true (brand gradient ring)
  tone = "lavender",
  // fallback bg tone
  style = {},
  ...rest
}) {
  const tones = {
    lavender: "var(--tint-lavender)",
    mint: "var(--tint-mint)",
    peach: "var(--tint-peach)",
    yellow: "var(--tint-yellow)"
  };
  const initial = (name || "?").trim().charAt(0).toUpperCase();
  const inner = /*#__PURE__*/React.createElement("div", {
    style: {
      width: size,
      height: size,
      borderRadius: "50%",
      overflow: "hidden",
      background: tones[tone] || tones.lavender,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      color: "var(--brand-purple)",
      fontFamily: "var(--font-sans)",
      fontWeight: 700,
      fontSize: size * 0.4,
      letterSpacing: "var(--tracking-snug)",
      flex: "none"
    }
  }, src ? /*#__PURE__*/React.createElement("img", {
    src: src,
    alt: name,
    style: {
      width: "100%",
      height: "100%",
      objectFit: "cover"
    }
  }) : initial);
  if (!ring) return /*#__PURE__*/React.createElement("div", _extends({
    style: style
  }, rest), inner);
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      padding: 2.5,
      borderRadius: "50%",
      background: "var(--grad-brand)",
      display: "inline-flex",
      ...style
    }
  }, rest), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: 2,
      borderRadius: "50%",
      background: "var(--white)",
      display: "inline-flex"
    }
  }, inner));
}
Object.assign(__ds_scope, { Avatar });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/display/Avatar.jsx", error: String((e && e.message) || e) }); }

// components/display/Badge.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Badge / Tag — small pill label. Soft (tinted) or solid fills,
 * keyed to a brand tone. Used for "Cadastro grátis", "Novo parceiro!",
 * "Recomendada", location chips, plan flags.
 */
function Badge({
  children,
  tone = "purple",
  // purple | pink | orange | green | gray | dark
  variant = "soft",
  // soft | solid | outline
  iconLeft = null,
  size = "md",
  // sm | md
  style = {},
  ...rest
}) {
  const palette = {
    purple: {
      solid: "var(--brand-purple)",
      soft: "var(--tint-lavender)",
      text: "var(--brand-purple)"
    },
    pink: {
      solid: "var(--brand-pink)",
      soft: "var(--tint-pink)",
      text: "var(--brand-pink)"
    },
    orange: {
      solid: "var(--brand-orange)",
      soft: "var(--tint-peach)",
      text: "var(--brand-orange-deep)"
    },
    green: {
      solid: "var(--success)",
      soft: "var(--tint-mint)",
      text: "var(--success)"
    },
    gray: {
      solid: "var(--gray-600)",
      soft: "var(--gray-100)",
      text: "var(--gray-600)"
    },
    dark: {
      solid: "var(--slate-heading)",
      soft: "var(--gray-100)",
      text: "var(--white)"
    }
  };
  const p = palette[tone] || palette.purple;
  const sizes = {
    sm: {
      fontSize: 11,
      padding: "3px 9px",
      gap: 4,
      icon: 12
    },
    md: {
      fontSize: 12.5,
      padding: "5px 12px",
      gap: 5,
      icon: 14
    }
  };
  const s = sizes[size] || sizes.md;
  const styles = {
    soft: {
      background: p.soft,
      color: p.text
    },
    solid: {
      background: p.solid,
      color: tone === "dark" ? "var(--white)" : "var(--white)"
    },
    outline: {
      background: "transparent",
      color: p.text,
      boxShadow: `inset 0 0 0 1.3px ${p.solid}`
    }
  };
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      display: "inline-flex",
      alignItems: "center",
      gap: s.gap,
      fontFamily: "var(--font-sans)",
      fontWeight: 600,
      fontSize: s.fontSize,
      letterSpacing: "var(--tracking-snug)",
      padding: s.padding,
      borderRadius: "var(--radius-pill)",
      lineHeight: 1,
      whiteSpace: "nowrap",
      ...styles[variant],
      ...style
    }
  }, rest), iconLeft && /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      width: s.icon,
      height: s.icon
    }
  }, iconLeft), children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/display/Badge.jsx", error: String((e && e.message) || e) }); }

// components/display/Card.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Card — the brand's default white, rounded, softly-shadowed container.
 */
function Card({
  children,
  padding = 24,
  radius = "var(--radius-xl)",
  elevation = "card",
  // none | sm | card | md | lg
  tone = "white",
  // white | sunken | lavender | mint | peach | yellow
  hairline = false,
  style = {},
  ...rest
}) {
  const shadows = {
    none: "none",
    sm: "var(--shadow-sm)",
    card: "var(--shadow-card)",
    md: "var(--shadow-md)",
    lg: "var(--shadow-lg)"
  };
  const tones = {
    white: "var(--surface-card)",
    sunken: "var(--surface-sunken)",
    lavender: "var(--tint-lavender)",
    mint: "var(--tint-mint)",
    peach: "var(--tint-peach)",
    yellow: "var(--tint-yellow)"
  };
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      background: tones[tone] || tone,
      borderRadius: radius,
      padding,
      boxShadow: hairline ? "var(--ring-hairline)" : shadows[elevation],
      boxSizing: "border-box",
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/display/Card.jsx", error: String((e && e.message) || e) }); }

// components/display/StatTile.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * StatTile — pastel tinted tile pairing a saturated icon with a big
 * number + label. Used for facility tiles ("Empresas", "Empregos",
 * "Ônibus") and city stat cards on the consumer home.
 */
function StatTile({
  value,
  label,
  icon = null,
  tone = "lavender",
  // lavender | mint | peach | yellow
  onClick,
  style = {},
  ...rest
}) {
  const map = {
    lavender: {
      bg: "var(--tint-lavender)",
      fg: "var(--brand-purple)"
    },
    mint: {
      bg: "var(--tint-mint)",
      fg: "var(--brand-mint)"
    },
    peach: {
      bg: "var(--tint-peach)",
      fg: "var(--brand-orange-deep)"
    },
    yellow: {
      bg: "var(--tint-yellow)",
      fg: "var(--brand-amber)"
    }
  };
  const t = map[tone] || map.lavender;
  return /*#__PURE__*/React.createElement("div", _extends({
    onClick: onClick,
    style: {
      background: t.bg,
      borderRadius: "var(--radius-lg)",
      padding: "18px 20px",
      display: "flex",
      alignItems: "center",
      gap: 14,
      cursor: onClick ? "pointer" : "default",
      transition: "transform var(--dur-base) var(--ease-out)",
      boxSizing: "border-box",
      ...style
    },
    onMouseEnter: e => onClick && (e.currentTarget.style.transform = "translateY(-2px)"),
    onMouseLeave: e => e.currentTarget.style.transform = "none"
  }, rest), icon && /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      width: 28,
      height: 28,
      color: t.fg,
      flex: "none"
    }
  }, icon), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gap: 2,
      minWidth: 0
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 800,
      fontSize: 24,
      color: "var(--ink)",
      letterSpacing: "var(--tracking-tight)",
      lineHeight: 1
    }
  }, value), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 500,
      fontSize: 13,
      color: "var(--gray-600)",
      letterSpacing: "var(--tracking-snug)",
      overflow: "hidden",
      textOverflow: "ellipsis",
      whiteSpace: "nowrap"
    }
  }, label)));
}
Object.assign(__ds_scope, { StatTile });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/display/StatTile.jsx", error: String((e && e.message) || e) }); }

// components/forms/Input.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Input — standard text field with optional leading icon.
 * Pill or rounded-rect, hairline border, focus ring in brand purple.
 */
function Input({
  value,
  onChange,
  placeholder = "",
  iconLeft = null,
  type = "text",
  shape = "rounded",
  // rounded | pill
  size = "md",
  // md | lg
  disabled = false,
  style = {},
  ...rest
}) {
  const [focus, setFocus] = React.useState(false);
  const sizes = {
    md: {
      h: 46,
      fs: 15,
      pad: 16
    },
    lg: {
      h: 56,
      fs: 16,
      pad: 20
    }
  };
  const s = sizes[size] || sizes.md;
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: 10,
      height: s.h,
      padding: `0 ${s.pad}px`,
      background: disabled ? "var(--gray-100)" : "var(--white)",
      borderRadius: shape === "pill" ? "var(--radius-pill)" : "var(--radius-sm)",
      boxShadow: focus ? "inset 0 0 0 1.5px var(--brand-purple)" : "inset 0 0 0 1px var(--gray-200)",
      transition: "box-shadow var(--dur-base) var(--ease-out)",
      boxSizing: "border-box",
      ...style
    }
  }, iconLeft && /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      width: 18,
      height: 18,
      color: "var(--gray-400)",
      flex: "none"
    }
  }, iconLeft), /*#__PURE__*/React.createElement("input", _extends({
    type: type,
    value: value,
    onChange: onChange,
    placeholder: placeholder,
    disabled: disabled,
    onFocus: () => setFocus(true),
    onBlur: () => setFocus(false),
    style: {
      flex: 1,
      minWidth: 0,
      border: "none",
      outline: "none",
      background: "transparent",
      fontFamily: "var(--font-sans)",
      fontSize: s.fs,
      fontWeight: 500,
      letterSpacing: "var(--tracking-snug)",
      color: "var(--ink)"
    }
  }, rest)));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Input.jsx", error: String((e && e.message) || e) }); }

// components/forms/SearchBar.jsx
try { (() => {
/**
 * SearchBar — Solutudo's hero search: a large glass pill with a leading
 * magnifier, optional mic, and a built-in "Buscar" affordance.
 */
function SearchBar({
  value,
  onChange,
  onSearch,
  placeholder = "Busque empresas",
  showMic = true,
  hint = "Pressione Enter",
  style = {}
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: 14,
      height: 76,
      padding: "0 14px 0 30px",
      background: "var(--glass-white)",
      backdropFilter: "var(--blur-glass)",
      WebkitBackdropFilter: "var(--blur-glass)",
      borderRadius: "var(--radius-pill)",
      boxShadow: "var(--ring-hairline), var(--shadow-md)",
      boxSizing: "border-box",
      ...style
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      color: "var(--gray-400)",
      flex: "none"
    }
  }, /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 24 24",
    width: "26",
    height: "26",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: "2.2",
    strokeLinecap: "round"
  }, /*#__PURE__*/React.createElement("circle", {
    cx: "11",
    cy: "11",
    r: "7"
  }), /*#__PURE__*/React.createElement("path", {
    d: "m20 20-3.2-3.2"
  }))), /*#__PURE__*/React.createElement("input", {
    value: value,
    onChange: onChange,
    placeholder: placeholder,
    onKeyDown: e => e.key === "Enter" && onSearch && onSearch(value),
    style: {
      flex: 1,
      minWidth: 0,
      border: "none",
      outline: "none",
      background: "transparent",
      fontFamily: "var(--font-sans)",
      fontSize: 22,
      fontWeight: 500,
      letterSpacing: "var(--tracking-snug)",
      color: "var(--ink)"
    }
  }), showMic && /*#__PURE__*/React.createElement("button", {
    type: "button",
    "aria-label": "Busca por voz",
    style: {
      border: "none",
      background: "transparent",
      cursor: "pointer",
      color: "var(--ink)",
      display: "inline-flex",
      padding: 8
    }
  }, /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 24 24",
    width: "24",
    height: "24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: "2",
    strokeLinecap: "round"
  }, /*#__PURE__*/React.createElement("rect", {
    x: "9",
    y: "2",
    width: "6",
    height: "12",
    rx: "3"
  }), /*#__PURE__*/React.createElement("path", {
    d: "M5 11a7 7 0 0 0 14 0M12 18v3"
  }))), /*#__PURE__*/React.createElement("button", {
    type: "button",
    onClick: () => onSearch && onSearch(value),
    style: {
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      gap: 1,
      border: "none",
      background: "transparent",
      cursor: "pointer",
      padding: "0 14px"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 700,
      fontSize: 24,
      color: "var(--ink)",
      letterSpacing: "var(--tracking-tight)",
      lineHeight: 1
    }
  }, "Buscar"), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 500,
      fontSize: 11,
      color: "var(--gray-400)"
    }
  }, hint)));
}
Object.assign(__ds_scope, { SearchBar });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/SearchBar.jsx", error: String((e && e.message) || e) }); }

// components/forms/SegmentedToggle.jsx
try { (() => {
/**
 * SegmentedToggle — pill switch with a sliding active segment.
 * Used for billing period (Mensal / Anual) and similar 2–3 way choices.
 */
function SegmentedToggle({
  options = [],
  // [{ value, label }]
  value,
  onChange,
  style = {}
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "inline-flex",
      padding: 4,
      background: "var(--white)",
      borderRadius: "var(--radius-pill)",
      boxShadow: "var(--ring-hairline)",
      gap: 2,
      ...style
    }
  }, options.map(opt => {
    const active = opt.value === value;
    return /*#__PURE__*/React.createElement("button", {
      key: opt.value,
      type: "button",
      onClick: () => onChange && onChange(opt.value),
      style: {
        border: "none",
        cursor: "pointer",
        fontFamily: "var(--font-sans)",
        fontWeight: 600,
        fontSize: 14,
        letterSpacing: "var(--tracking-snug)",
        padding: "9px 22px",
        borderRadius: "var(--radius-pill)",
        background: active ? "var(--brand-purple)" : "transparent",
        color: active ? "var(--white)" : "var(--gray-500)",
        transition: "background var(--dur-base) var(--ease-out), color var(--dur-base) var(--ease-out)"
      }
    }, opt.label);
  }));
}
Object.assign(__ds_scope, { SegmentedToggle });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/SegmentedToggle.jsx", error: String((e && e.message) || e) }); }

// components/marketing/FeedItem.jsx
try { (() => {
/**
 * FeedItem — a single entry in the city "Movimento" activity timeline:
 * an icon chip with a small "+" badge, a title, optional location +
 * status chips, and a timestamp.
 */
function FeedItem({
  title,
  timestamp,
  icon = null,
  iconTone = "purple",
  // purple | orange | teal
  badges = null,
  // React node (e.g. <Badge/> chips)
  titleColor = null,
  style = {}
}) {
  const tones = {
    purple: {
      bg: "var(--tint-lavender)",
      fg: "var(--brand-purple)",
      dot: "var(--brand-purple)"
    },
    orange: {
      bg: "var(--tint-peach)",
      fg: "var(--brand-orange-deep)",
      dot: "var(--brand-orange)"
    },
    teal: {
      bg: "#CFF7EE",
      fg: "#0FA98A",
      dot: "#0FA98A"
    }
  };
  const t = tones[iconTone] || tones.purple;
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: 14,
      background: "var(--white)",
      borderRadius: "var(--radius-lg)",
      boxShadow: "var(--shadow-card)",
      padding: "16px 18px",
      boxSizing: "border-box",
      ...style
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      flex: "none"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      width: 48,
      height: 48,
      borderRadius: "50%",
      background: t.bg,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      color: t.fg
    }
  }, icon), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      top: -2,
      right: -2,
      width: 20,
      height: 20,
      borderRadius: "50%",
      background: t.dot,
      color: "var(--white)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      fontSize: 13,
      fontWeight: 700,
      boxShadow: "0 0 0 2.5px var(--white)"
    }
  }, "+")), /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      minWidth: 0,
      display: "flex",
      flexDirection: "column",
      gap: 7
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 15,
      fontWeight: 700,
      color: titleColor || "var(--slate-heading)",
      letterSpacing: "var(--tracking-snug)",
      lineHeight: 1.2
    }
  }, title), badges && /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: 8,
      flexWrap: "wrap",
      alignItems: "center"
    }
  }, badges)), timestamp && /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 13,
      color: "var(--gray-400)",
      fontWeight: 500,
      letterSpacing: "var(--tracking-snug)",
      flex: "none",
      alignSelf: "flex-start"
    }
  }, timestamp));
}
Object.assign(__ds_scope, { FeedItem });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/marketing/FeedItem.jsx", error: String((e && e.message) || e) }); }

// components/marketing/PlanCard.jsx
try { (() => {
/**
 * PlanCard — a pricing tier card for "Planos e Preços".
 * Each tier owns a color; the card shows label, price, name, CTA,
 * description and a checked feature list.
 */
function PlanCard({
  name,
  price,
  // e.g. "R$ 29,90/mês" or "Grátis"
  tone = "purple",
  // ink | green | purple | pink | orange
  subtitle = null,
  // e.g. "+ Social Media"
  description,
  featuresLabel = "Recursos:",
  features = [],
  ctaLabel = "Mudar para este plano",
  current = false,
  onSelect,
  style = {}
}) {
  const tones = {
    ink: "var(--ink)",
    green: "var(--success)",
    purple: "var(--brand-purple)",
    pink: "var(--brand-pink)",
    orange: "var(--brand-orange)"
  };
  const accent = tones[tone] || tones.purple;
  const Check = () => /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 24 24",
    width: "17",
    height: "17",
    fill: "none",
    stroke: accent,
    strokeWidth: "3",
    strokeLinecap: "round",
    strokeLinejoin: "round",
    style: {
      flex: "none",
      marginTop: 1
    }
  }, /*#__PURE__*/React.createElement("path", {
    d: "M20 6 9 17l-5-5"
  }));
  return /*#__PURE__*/React.createElement("div", {
    style: {
      background: "var(--surface-card)",
      borderRadius: "var(--radius-xl)",
      boxShadow: "var(--shadow-card)",
      padding: 28,
      display: "flex",
      flexDirection: "column",
      gap: 18,
      boxSizing: "border-box",
      ...style
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      justifyContent: "space-between",
      alignItems: "baseline"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 14,
      color: "var(--gray-400)",
      fontWeight: 500,
      letterSpacing: "var(--tracking-snug)"
    }
  }, "Plano"), price && /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 16,
      fontWeight: 700,
      color: "var(--ink)",
      letterSpacing: "var(--tracking-snug)"
    }
  }, price)), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h3", {
    style: {
      fontSize: 22,
      fontWeight: 700,
      color: accent,
      letterSpacing: "var(--tracking-tight)",
      margin: 0
    }
  }, name), subtitle && /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: 14,
      fontWeight: 600,
      color: accent,
      marginTop: 2,
      letterSpacing: "var(--tracking-snug)"
    }
  }, subtitle)), /*#__PURE__*/React.createElement("button", {
    type: "button",
    disabled: current,
    onClick: onSelect,
    style: {
      border: "none",
      borderRadius: "var(--radius-pill)",
      padding: "15px 20px",
      fontFamily: "var(--font-sans)",
      fontWeight: 600,
      fontSize: 15,
      letterSpacing: "var(--tracking-snug)",
      cursor: current ? "default" : "pointer",
      background: current ? "var(--gray-300)" : "var(--ink)",
      color: "var(--white)",
      transition: "filter var(--dur-base) var(--ease-out)"
    },
    onMouseEnter: e => {
      if (!current) e.currentTarget.style.filter = "brightness(1.25)";
    },
    onMouseLeave: e => {
      e.currentTarget.style.filter = "none";
    }
  }, current ? "Seu plano atual" : ctaLabel), description && /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 14,
      color: "var(--gray-500)",
      letterSpacing: "var(--tracking-snug)",
      lineHeight: 1.45,
      margin: 0
    }
  }, description), /*#__PURE__*/React.createElement("div", {
    style: {
      height: 1,
      background: "var(--gray-150)"
    }
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: 12
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 13,
      color: "var(--gray-400)",
      fontWeight: 500
    }
  }, featuresLabel), features.map((f, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    style: {
      display: "flex",
      gap: 10,
      alignItems: "flex-start"
    }
  }, /*#__PURE__*/React.createElement(Check, null), /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 14,
      color: "var(--ink)",
      letterSpacing: "var(--tracking-snug)",
      lineHeight: 1.4
    }
  }, f)))));
}
Object.assign(__ds_scope, { PlanCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/marketing/PlanCard.jsx", error: String((e && e.message) || e) }); }

// ui_kits/business/app.jsx
try { (() => {
// Business kit — app shell. window-global Babel.
function BizApp() {
  const [screen, setScreen] = React.useState("landing"); // landing | dashboard
  const Landing = window.BizLanding;
  const Dashboard = window.BizDashboard;
  return /*#__PURE__*/React.createElement("div", {
    className: "bizapp"
  }, screen === "landing" ? /*#__PURE__*/React.createElement(Landing, {
    onEnter: () => setScreen("dashboard"),
    onRegister: () => setScreen("dashboard")
  }) : /*#__PURE__*/React.createElement(Dashboard, {
    onExit: () => setScreen("landing")
  }));
}
ReactDOM.createRoot(document.getElementById("root")).render(/*#__PURE__*/React.createElement(BizApp, null));
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/business/app.jsx", error: String((e && e.message) || e) }); }

// ui_kits/business/dashboard.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
// Business kit — Área do Empresário dashboard. window-global Babel.
const {
  Button: DBtn,
  Card: DCard,
  Badge: DBadge,
  Avatar: DAv,
  StatTile: DStat,
  SegmentedToggle: DSeg
} = window;
const DIc = window.SolIcons;
const DPlan = window.BizPlanCard;
function DashNav({
  tab,
  setTab,
  onExit
}) {
  const tabs = [["inicio", "Início"], ["perfil", "Perfil da Empresa"], ["resultados", "Resultados"], ["planos", "Planos e Preços"]];
  return /*#__PURE__*/React.createElement("header", {
    className: "dash-nav"
  }, /*#__PURE__*/React.createElement("button", {
    className: "dash-logo",
    onClick: onExit
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/logo-solutudo.png",
    alt: "Solutudo"
  }), /*#__PURE__*/React.createElement("span", null, "\xC1rea do", /*#__PURE__*/React.createElement("br", null), "Empres\xE1rio")), /*#__PURE__*/React.createElement("nav", {
    className: "dash-tabs"
  }, tabs.map(([k, l]) => /*#__PURE__*/React.createElement("button", {
    key: k,
    "data-active": tab === k ? "" : undefined,
    onClick: () => setTab(k)
  }, l))), /*#__PURE__*/React.createElement("div", {
    className: "dash-right"
  }, /*#__PURE__*/React.createElement("button", {
    className: "dash-support"
  }, /*#__PURE__*/React.createElement(DIc.Whatsapp, {
    w: 18
  }), " Suporte"), /*#__PURE__*/React.createElement(DAv, {
    src: "../../assets/avatar-b.png",
    name: "E",
    size: 38
  })));
}

/* ---- Início ---- */
function TabInicio({
  setTab
}) {
  return /*#__PURE__*/React.createElement("div", {
    className: "tab-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "dash-hero"
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h1", {
    className: "dash-title"
  }, "Ol\xE1, ", /*#__PURE__*/React.createElement("span", {
    className: "sol-display sol-gradient-text"
  }, "Padaria P\xE3o Quente")), /*#__PURE__*/React.createElement("p", {
    className: "dash-subtitle"
  }, "Veja como sua empresa est\xE1 performando na Solutudo.")), /*#__PURE__*/React.createElement(DBtn, {
    variant: "primary",
    iconRight: /*#__PURE__*/React.createElement(DIc.Arrow, {
      w: 18
    }),
    onClick: () => setTab("planos")
  }, "Seja Destaque")), /*#__PURE__*/React.createElement("div", {
    className: "dash-grid"
  }, /*#__PURE__*/React.createElement(DCard, {
    padding: 24,
    elevation: "card",
    style: {
      gridColumn: "span 2"
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "profile-strength"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ps-head"
  }, /*#__PURE__*/React.createElement("span", {
    className: "ps-title"
  }, "Perfil 80% completo"), /*#__PURE__*/React.createElement(DBadge, {
    tone: "purple"
  }, "3 fotos restantes")), /*#__PURE__*/React.createElement("div", {
    className: "ps-bar"
  }, /*#__PURE__*/React.createElement("div", {
    className: "ps-fill",
    style: {
      width: "80%"
    }
  })), /*#__PURE__*/React.createElement("p", {
    className: "ps-note"
  }, "Complete seu perfil para aparecer mais nas buscas e nas IAs."), /*#__PURE__*/React.createElement(DBtn, {
    variant: "secondary",
    size: "sm",
    iconLeft: /*#__PURE__*/React.createElement(DIc.Edit, {
      w: 16
    }),
    style: {
      marginTop: 4
    }
  }, "Editar cadastro"))), /*#__PURE__*/React.createElement(DStat, {
    tone: "lavender",
    value: "1.284",
    label: "Visualiza\xE7\xF5es no m\xEAs",
    icon: /*#__PURE__*/React.createElement(DIc.Chart, null)
  }), /*#__PURE__*/React.createElement(DStat, {
    tone: "mint",
    value: "342",
    label: "Cliques no WhatsApp",
    icon: /*#__PURE__*/React.createElement(DIc.Whatsapp, null)
  })), /*#__PURE__*/React.createElement("h2", {
    className: "dash-section"
  }, "Movimento recente"), /*#__PURE__*/React.createElement("div", {
    className: "dash-recent"
  }, [{
    ic: /*#__PURE__*/React.createElement(DIc.Whatsapp, {
      w: 20
    }),
    tone: "mint",
    t: "Novo contato pelo WhatsApp",
    time: "Há 8 min"
  }, {
    ic: /*#__PURE__*/React.createElement(DIc.Search, {
      w: 20
    }),
    tone: "lavender",
    t: "Sua empresa apareceu em 12 buscas",
    time: "Há 1 hora"
  }, {
    ic: /*#__PURE__*/React.createElement(DIc.Star, {
      w: 20
    }),
    tone: "peach",
    t: "Você recebeu uma nova recomendação",
    time: "Ontem"
  }].map((r, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    className: "recent-row"
  }, /*#__PURE__*/React.createElement("span", {
    className: "recent-ic",
    "data-tone": r.tone
  }, r.ic), /*#__PURE__*/React.createElement("span", {
    className: "recent-t"
  }, r.t), /*#__PURE__*/React.createElement("span", {
    className: "recent-time"
  }, r.time)))));
}

/* ---- Resultados ---- */
function TabResultados() {
  const bars = [40, 58, 47, 72, 65, 88, 79];
  const days = ["S", "T", "Q", "Q", "S", "S", "D"];
  return /*#__PURE__*/React.createElement("div", {
    className: "tab-wrap"
  }, /*#__PURE__*/React.createElement("h1", {
    className: "dash-title",
    style: {
      marginBottom: 6
    }
  }, "Resultados"), /*#__PURE__*/React.createElement("p", {
    className: "dash-subtitle",
    style: {
      marginBottom: 24
    }
  }, "Seu desempenho nos \xFAltimos 7 dias."), /*#__PURE__*/React.createElement("div", {
    className: "dash-grid"
  }, /*#__PURE__*/React.createElement(DStat, {
    tone: "lavender",
    value: "1.284",
    label: "Visualiza\xE7\xF5es",
    icon: /*#__PURE__*/React.createElement(DIc.Chart, null)
  }), /*#__PURE__*/React.createElement(DStat, {
    tone: "mint",
    value: "342",
    label: "Cliques no WhatsApp",
    icon: /*#__PURE__*/React.createElement(DIc.Whatsapp, null)
  }), /*#__PURE__*/React.createElement(DStat, {
    tone: "peach",
    value: "96",
    label: "Cliques no telefone",
    icon: /*#__PURE__*/React.createElement(DIc.Phone, null)
  }), /*#__PURE__*/React.createElement(DStat, {
    tone: "yellow",
    value: "18",
    label: "Acessos ao site",
    icon: /*#__PURE__*/React.createElement(DIc.Globe, null)
  })), /*#__PURE__*/React.createElement(DCard, {
    padding: 28,
    elevation: "card",
    style: {
      marginTop: 16
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "chart-head"
  }, /*#__PURE__*/React.createElement("span", {
    className: "chart-title"
  }, "Visualiza\xE7\xF5es por dia"), /*#__PURE__*/React.createElement(DBadge, {
    tone: "green"
  }, "+24% vs. semana anterior")), /*#__PURE__*/React.createElement("div", {
    className: "chart"
  }, bars.map((h, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    className: "chart-col"
  }, /*#__PURE__*/React.createElement("div", {
    className: "chart-bar",
    style: {
      height: h + "%"
    }
  }), /*#__PURE__*/React.createElement("span", null, days[i]))))));
}

/* ---- Planos ---- */
function TabPlanos() {
  const [period, setPeriod] = React.useState("mensal");
  const mult = period === "anual" ? 0.8 : 1;
  const fmt = v => v === 0 ? "Grátis" : "R$ " + (v * mult).toFixed(2).replace(".", ",") + (period === "anual" ? "/mês" : "/mês");
  const plans = [{
    tone: "ink",
    name: "Gratuito",
    price: null,
    description: "Presença básica para ser encontrado no digital.",
    featuresLabel: "Recursos:",
    features: ["Cadastro na Solutudo", "Dados de contato", "Até 3 fotos", "Indexação básica em Google e ChatGPT*"]
  }, {
    tone: "green",
    name: "Essencial",
    price: fmt(29.90),
    description: "Aumente as chances de ser encontrado no digital.",
    featuresLabel: "Tudo do plano anterior, mais:",
    features: ["Site básico", "Página Solutudo", "Até 100 fotos", "Produtos, notícias e + conteúdos", "Suporte Solutudo sob demanda"],
    current: true
  }, {
    tone: "purple",
    name: "Destaque",
    price: fmt(189.90),
    description: "Gere valor com presença constante nos principais pontos de contatos digitais.",
    featuresLabel: "Tudo dos planos anteriores, mais:",
    features: ["Site profissional personalizado", "Página Solutudo personalizada", "Seu perfil no Google Meu Negócio", "Relatório mensal de acessos"]
  }, {
    tone: "pink",
    name: "Destaque Exponencial",
    subtitle: "+ Social Media",
    price: fmt(499.90),
    description: "Social media e 4 atualizações mensais em todos os pontos de contatos digitais.",
    featuresLabel: "Tudo dos planos anteriores, mais:",
    features: ["Social Media profissional, 4 atualizações/mês", "Site profissional + 4 atualizações", "Página Solutudo + 4 atualizações"]
  }, {
    tone: "orange",
    name: "Destaque Exponencial",
    subtitle: "+ Social Media Completo",
    price: fmt(1299.90),
    description: "Social media e 8 atualizações mensais em todos os pontos de contatos digitais.",
    featuresLabel: "Tudo dos planos anteriores, mais:",
    features: ["Social Media com criações personalizadas", "Site profissional + 8 atualizações", "Página Solutudo + 8 atualizações"]
  }];
  return /*#__PURE__*/React.createElement("div", {
    className: "tab-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "planos-head"
  }, /*#__PURE__*/React.createElement("h1", {
    className: "dash-title"
  }, "Planos e Pre\xE7os"), /*#__PURE__*/React.createElement("p", {
    className: "dash-subtitle"
  }, "Planos para todas as etapas do seu neg\xF3cio."), /*#__PURE__*/React.createElement("div", {
    className: "planos-toggle"
  }, /*#__PURE__*/React.createElement("span", null, "Forma de pagamento:"), /*#__PURE__*/React.createElement(DSeg, {
    value: period,
    onChange: setPeriod,
    options: [{
      value: "mensal",
      label: "Mensal"
    }, {
      value: "anual",
      label: "Anual"
    }]
  }), /*#__PURE__*/React.createElement("span", {
    className: "planos-discount"
  }, "20% de desconto no plano Anual"))), /*#__PURE__*/React.createElement("div", {
    className: "planos-grid"
  }, plans.map((p, i) => /*#__PURE__*/React.createElement(DPlan, _extends({
    key: i
  }, p)))));
}
function Dashboard({
  onExit
}) {
  const [tab, setTab] = React.useState("inicio");
  return /*#__PURE__*/React.createElement("div", {
    className: "dashboard"
  }, /*#__PURE__*/React.createElement(DashNav, {
    tab: tab,
    setTab: setTab,
    onExit: onExit
  }), /*#__PURE__*/React.createElement("main", {
    className: "dash-main"
  }, (tab === "inicio" || tab === "perfil") && /*#__PURE__*/React.createElement(TabInicio, {
    setTab: setTab
  }), tab === "resultados" && /*#__PURE__*/React.createElement(TabResultados, null), tab === "planos" && /*#__PURE__*/React.createElement(TabPlanos, null)));
}
window.BizDashboard = Dashboard;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/business/dashboard.jsx", error: String((e && e.message) || e) }); }

// ui_kits/business/landing.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
// Business kit — Landing (marketing) screen. window-global Babel.
const {
  Button: LBtn,
  Card: LCard
} = window;
const LIc = window.SolIcons;
function EngineChip({
  label,
  glyph,
  color
}) {
  return /*#__PURE__*/React.createElement("div", {
    className: "engine-chip"
  }, /*#__PURE__*/React.createElement("span", {
    className: "engine-glyph",
    style: {
      color
    }
  }, glyph), /*#__PURE__*/React.createElement("span", null, label));
}
function Landing({
  onEnter,
  onRegister
}) {
  const engines = [{
    label: "Google",
    glyph: "G",
    color: "#4285F4"
  }, {
    label: "ChatGPT",
    glyph: "✦",
    color: "#10A37F"
  }, {
    label: "Gemini",
    glyph: "◆",
    color: "#8E6FF7"
  }, {
    label: "WhatsApp",
    glyph: "✆",
    color: "#25D366"
  }, {
    label: "Bing",
    glyph: "b",
    color: "#0078D4"
  }, {
    label: "Claude",
    glyph: "✳",
    color: "#D97757"
  }];
  const benefits = [{
    icon: /*#__PURE__*/React.createElement(LIc.Store, {
      w: 30
    }),
    title: "Cadastro Grátis",
    body: "Cadastre sua empresa grátis na Solutudo. Leva menos de 1 minuto!"
  }, {
    icon: /*#__PURE__*/React.createElement(LIc.Search, {
      w: 30
    }),
    title: "Sua empresa na internet",
    body: "Aumente suas chances de ser encontrado no Google, Bing, ChatGPT e mais IAs."
  }, {
    icon: /*#__PURE__*/React.createElement(LIc.Globe, {
      w: 30
    }),
    title: "Seu link próprio",
    body: "suaempresa.solutudo.com.br — uma página só sua para divulgar onde quiser."
  }];
  return /*#__PURE__*/React.createElement("div", {
    className: "landing"
  }, /*#__PURE__*/React.createElement("header", {
    className: "lp-nav"
  }, /*#__PURE__*/React.createElement("div", {
    className: "lp-logo"
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/logo-solutudo.png",
    alt: "Solutudo"
  }), /*#__PURE__*/React.createElement("span", null, "O maior guia de e", /*#__PURE__*/React.createElement("br", null), "para empresas do Brasil.")), /*#__PURE__*/React.createElement("nav", {
    className: "lp-nav-center"
  }, /*#__PURE__*/React.createElement("span", {
    "data-active": ""
  }, "COMECE"), /*#__PURE__*/React.createElement("span", null, "COMO FUNCIONA"), /*#__PURE__*/React.createElement("span", null, "BENEF\xCDCIOS"), /*#__PURE__*/React.createElement("span", null, "CADASTRO")), /*#__PURE__*/React.createElement(LBtn, {
    variant: "dark",
    onClick: onRegister
  }, "Cadastrar gr\xE1tis")), /*#__PURE__*/React.createElement("section", {
    className: "lp-hero"
  }, /*#__PURE__*/React.createElement("h1", {
    className: "lp-h1"
  }, /*#__PURE__*/React.createElement("span", {
    className: "sol-display sol-gradient-text"
  }, "Cadastre gr\xE1tis"), " sua empresa", /*#__PURE__*/React.createElement("br", null), /*#__PURE__*/React.createElement("span", {
    className: "lp-h1-dark"
  }, "e aumente suas chances de receber contatos em Sorocaba e regi\xE3o.")), /*#__PURE__*/React.createElement("p", {
    className: "lp-sub"
  }, "Seu neg\xF3cio na Solutudo, o maior guia de empresas do Brasil."), /*#__PURE__*/React.createElement("div", {
    className: "lp-cta"
  }, /*#__PURE__*/React.createElement(LBtn, {
    variant: "secondary",
    size: "lg",
    onClick: onEnter
  }, "Saiba mais"), /*#__PURE__*/React.createElement(LBtn, {
    variant: "primary",
    size: "lg",
    iconRight: /*#__PURE__*/React.createElement(LIc.Arrow, {
      w: 20
    }),
    onClick: onRegister
  }, "Cadastrar empresa")), /*#__PURE__*/React.createElement("div", {
    className: "lp-diagram"
  }, /*#__PURE__*/React.createElement("div", {
    className: "lp-engines lp-engines-l"
  }, engines.slice(0, 3).map(e => /*#__PURE__*/React.createElement(EngineChip, _extends({
    key: e.label
  }, e)))), /*#__PURE__*/React.createElement("div", {
    className: "lp-bizcard"
  }, /*#__PURE__*/React.createElement("div", {
    className: "pf-rainbow"
  }), /*#__PURE__*/React.createElement("div", {
    className: "lp-bizcard-in"
  }, /*#__PURE__*/React.createElement("img", {
    className: "lp-bizcard-logo",
    src: "../../assets/logo-solutudo.png",
    alt: ""
  }), /*#__PURE__*/React.createElement("span", {
    className: "lp-bizcard-name"
  }, "Sua Empresa"), /*#__PURE__*/React.createElement("button", {
    className: "lp-bizcard-wpp"
  }, /*#__PURE__*/React.createElement(LIc.Whatsapp, {
    w: 16
  }), " Chamar no WhatsApp"), /*#__PURE__*/React.createElement("div", {
    className: "lp-bizcard-row"
  }, /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement(LIc.Phone, {
    w: 13
  }), " Telefone"), /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement(LIc.Pin, {
    w: 13
  }), " Endere\xE7o")))), /*#__PURE__*/React.createElement("div", {
    className: "lp-engines lp-engines-r"
  }, engines.slice(3).map(e => /*#__PURE__*/React.createElement(EngineChip, _extends({
    key: e.label
  }, e)))))), /*#__PURE__*/React.createElement("section", {
    className: "lp-benefits"
  }, benefits.map((b, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    className: "lp-benefit"
  }, /*#__PURE__*/React.createElement("span", {
    className: "lp-benefit-ic"
  }, b.icon), /*#__PURE__*/React.createElement("h3", null, b.title), /*#__PURE__*/React.createElement("p", null, b.body)))), /*#__PURE__*/React.createElement("section", {
    className: "lp-press"
  }, /*#__PURE__*/React.createElement("span", {
    className: "lp-press-label"
  }, "Somos a ponte entre a popula\xE7\xE3o e as empresas \u2014 e a Solutudo \xE9 not\xEDcia em:"), /*#__PURE__*/React.createElement("div", {
    className: "lp-press-logos"
  }, /*#__PURE__*/React.createElement("b", null, "ESTAD\xC3O"), /*#__PURE__*/React.createElement("b", {
    style: {
      fontStyle: "italic"
    }
  }, "exame."), /*#__PURE__*/React.createElement("b", null, "GAZETA DO POVO"), /*#__PURE__*/React.createElement("b", null, "Empresas&Neg\xF3cios")), /*#__PURE__*/React.createElement(LBtn, {
    variant: "primary",
    size: "lg",
    iconRight: /*#__PURE__*/React.createElement(LIc.Arrow, {
      w: 20
    }),
    onClick: onEnter,
    style: {
      marginTop: 28
    }
  }, "Acessar \xE1rea do empres\xE1rio")));
}
window.BizLanding = Landing;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/business/landing.jsx", error: String((e && e.message) || e) }); }

// ui_kits/business/plancard.jsx
try { (() => {
// Business kit — PlanCard (window-global Babel)
function PlanCard({
  name,
  price,
  tone = "purple",
  subtitle,
  description,
  featuresLabel = "Recursos:",
  features = [],
  ctaLabel = "Mudar para este plano",
  current,
  onSelect
}) {
  const A = {
    ink: "var(--ink)",
    green: "var(--success)",
    purple: "var(--brand-purple)",
    pink: "var(--brand-pink)",
    orange: "var(--brand-orange)"
  }[tone];
  const Check = () => /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 24 24",
    width: "17",
    height: "17",
    fill: "none",
    stroke: A,
    strokeWidth: "3",
    strokeLinecap: "round",
    strokeLinejoin: "round",
    style: {
      flex: "none",
      marginTop: 1
    }
  }, /*#__PURE__*/React.createElement("path", {
    d: "M20 6 9 17l-5-5"
  }));
  const [h, setH] = React.useState(false);
  return /*#__PURE__*/React.createElement("div", {
    className: "plan-card"
  }, /*#__PURE__*/React.createElement("div", {
    className: "plan-head"
  }, /*#__PURE__*/React.createElement("span", {
    className: "plan-plano"
  }, "Plano"), price && /*#__PURE__*/React.createElement("span", {
    className: "plan-price"
  }, price)), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h3", {
    className: "plan-name",
    style: {
      color: A
    }
  }, name), subtitle && /*#__PURE__*/React.createElement("div", {
    className: "plan-sub",
    style: {
      color: A
    }
  }, subtitle)), /*#__PURE__*/React.createElement("button", {
    type: "button",
    disabled: current,
    onClick: onSelect,
    onMouseEnter: () => setH(true),
    onMouseLeave: () => setH(false),
    className: "plan-cta",
    style: {
      background: current ? "var(--gray-300)" : "var(--ink)",
      cursor: current ? "default" : "pointer",
      filter: h && !current ? "brightness(1.3)" : "none"
    }
  }, current ? "Seu plano atual" : ctaLabel), description && /*#__PURE__*/React.createElement("p", {
    className: "plan-desc"
  }, description), /*#__PURE__*/React.createElement("div", {
    className: "plan-divider"
  }), /*#__PURE__*/React.createElement("div", {
    className: "plan-feats"
  }, /*#__PURE__*/React.createElement("span", {
    className: "plan-feats-label"
  }, featuresLabel), features.map((f, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    className: "plan-feat"
  }, /*#__PURE__*/React.createElement(Check, null), /*#__PURE__*/React.createElement("span", null, f)))), /*#__PURE__*/React.createElement("button", {
    className: "plan-detail"
  }, "Ver detalhes ", /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 24 24",
    width: "16",
    height: "16",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: "2.2",
    strokeLinecap: "round",
    strokeLinejoin: "round"
  }, /*#__PURE__*/React.createElement("path", {
    d: "M5 12h14M13 6l6 6-6 6"
  }))));
}
window.BizPlanCard = PlanCard;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/business/plancard.jsx", error: String((e && e.message) || e) }); }

// ui_kits/consumer-search/app.jsx
try { (() => {
// Consumer Search — app shell & routing (window-global Babel)
const {
  Home,
  Results,
  Profile
} = window.ConsumerScreens;
const MovimentoOverlay = window.Movimento;
function App() {
  const [screen, setScreen] = React.useState("home"); // home | results | profile
  const [q, setQ] = React.useState("");
  const [biz, setBiz] = React.useState(null);
  const [mov, setMov] = React.useState(false);
  const goSearch = () => setScreen("results");
  const goHome = () => setScreen("home");
  const goBiz = b => {
    setBiz(b);
    setScreen("profile");
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "app"
  }, screen === "home" && /*#__PURE__*/React.createElement(Home, {
    q: q,
    setQ: setQ,
    onSearch: goSearch,
    onMov: () => setMov(true),
    onBiz: goBiz
  }), screen === "results" && /*#__PURE__*/React.createElement(Results, {
    q: q,
    onBack: goHome,
    onBiz: goBiz
  }), screen === "profile" && /*#__PURE__*/React.createElement(Profile, {
    biz: biz,
    onBack: () => setScreen("results")
  }), mov && /*#__PURE__*/React.createElement(MovimentoOverlay, {
    onClose: () => setMov(false)
  }));
}
ReactDOM.createRoot(document.getElementById("root")).render(/*#__PURE__*/React.createElement(App, null));
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/consumer-search/app.jsx", error: String((e && e.message) || e) }); }

// ui_kits/consumer-search/movimento.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
// Consumer Search — Movimento activity feed overlay (window-global Babel)
const {
  Badge: MBadge
} = window;
const MIc = window.SolIcons;
function FeedItem({
  title,
  timestamp,
  icon,
  iconTone = "purple",
  badges,
  titleColor
}) {
  const T = {
    purple: {
      bg: "var(--tint-lavender)",
      fg: "var(--brand-purple)",
      dot: "var(--brand-purple)"
    },
    orange: {
      bg: "var(--tint-peach)",
      fg: "var(--brand-orange-deep)",
      dot: "var(--brand-orange)"
    },
    teal: {
      bg: "#CFF7EE",
      fg: "#0FA98A",
      dot: "#0FA98A"
    }
  }[iconTone];
  return /*#__PURE__*/React.createElement("div", {
    className: "feed-item"
  }, /*#__PURE__*/React.createElement("div", {
    className: "fi-icon-wrap"
  }, /*#__PURE__*/React.createElement("div", {
    className: "fi-icon",
    style: {
      background: T.bg,
      color: T.fg
    }
  }, icon), /*#__PURE__*/React.createElement("div", {
    className: "fi-plus",
    style: {
      background: T.dot
    }
  }, "+")), /*#__PURE__*/React.createElement("div", {
    className: "fi-body"
  }, /*#__PURE__*/React.createElement("span", {
    className: "fi-title",
    style: {
      color: titleColor || "var(--slate-heading)"
    }
  }, title), badges && /*#__PURE__*/React.createElement("div", {
    className: "fi-badges"
  }, badges)), /*#__PURE__*/React.createElement("span", {
    className: "fi-time"
  }, timestamp));
}
function Movimento({
  onClose
}) {
  const pin = /*#__PURE__*/React.createElement(MBadge, {
    tone: "gray",
    iconLeft: /*#__PURE__*/React.createElement(MIc.Pin, null)
  }, "Nome da cidade");
  const left = [{
    icon: /*#__PURE__*/React.createElement(MIc.Briefcase, {
      w: 22
    }),
    iconTone: "teal",
    titleColor: "#0FA98A",
    title: "+1 Vaga: Assistente de Contabilidade",
    timestamp: "Há 3 seg",
    badges: /*#__PURE__*/React.createElement(MBadge, {
      tone: "gray",
      iconLeft: /*#__PURE__*/React.createElement(MIc.Pin, null)
    }, "Solutudo: S\xE3o Manuel")
  }, {
    icon: /*#__PURE__*/React.createElement(MIc.Store, {
      w: 22
    }),
    title: "Nome da Empresa",
    timestamp: "Há 1 min",
    badges: /*#__PURE__*/React.createElement(React.Fragment, null, pin, /*#__PURE__*/React.createElement(MBadge, {
      tone: "purple"
    }, "Cadastro gr\xE1tis"))
  }, {
    icon: /*#__PURE__*/React.createElement(MIc.Box, {
      w: 22
    }),
    iconTone: "orange",
    titleColor: "var(--brand-orange-deep)",
    title: "+21 produtos cadastrados",
    timestamp: "Há 1 min",
    badges: pin
  }, {
    icon: /*#__PURE__*/React.createElement(MIc.Store, {
      w: 22
    }),
    title: "Nome da Empresa",
    timestamp: "Há 1h30",
    badges: /*#__PURE__*/React.createElement(React.Fragment, null, pin, /*#__PURE__*/React.createElement(MBadge, {
      tone: "dark",
      variant: "solid",
      iconLeft: /*#__PURE__*/React.createElement(MIc.Star, null)
    }, "Novo parceiro!"))
  }];
  const right = [{
    icon: /*#__PURE__*/React.createElement(MIc.Store, {
      w: 22
    }),
    title: "Nome da Empresa",
    timestamp: "Há 5 seg",
    badges: /*#__PURE__*/React.createElement(React.Fragment, null, pin, /*#__PURE__*/React.createElement(MBadge, {
      tone: "dark",
      variant: "solid",
      iconLeft: /*#__PURE__*/React.createElement(MIc.Star, null)
    }, "Novo parceiro!"))
  }, {
    icon: /*#__PURE__*/React.createElement(MIc.Store, {
      w: 22
    }),
    title: "Nome da Empresa",
    timestamp: "Há 1 min",
    badges: /*#__PURE__*/React.createElement(React.Fragment, null, pin, /*#__PURE__*/React.createElement(MBadge, {
      tone: "purple"
    }, "Cadastro gr\xE1tis"))
  }, {
    icon: /*#__PURE__*/React.createElement(MIc.Box, {
      w: 22
    }),
    iconTone: "orange",
    titleColor: "var(--brand-orange-deep)",
    title: "+205 produtos cadastrados",
    timestamp: "Há 1 hora",
    badges: /*#__PURE__*/React.createElement(MBadge, {
      tone: "gray",
      iconLeft: /*#__PURE__*/React.createElement(MIc.Pin, null)
    }, "Solutudo: S\xE3o Manuel")
  }, {
    icon: /*#__PURE__*/React.createElement(MIc.Briefcase, {
      w: 22
    }),
    iconTone: "teal",
    titleColor: "#0FA98A",
    title: "+1 Vaga: Assistente de Contabilidade",
    timestamp: "12h56",
    badges: pin
  }];
  return /*#__PURE__*/React.createElement("div", {
    className: "mov-overlay",
    onClick: onClose
  }, /*#__PURE__*/React.createElement("div", {
    className: "mov-sheet",
    onClick: e => e.stopPropagation()
  }, /*#__PURE__*/React.createElement("button", {
    className: "mov-close",
    onClick: onClose
  }, /*#__PURE__*/React.createElement(MIc.Close, {
    w: 22
  })), /*#__PURE__*/React.createElement("h2", {
    className: "mov-title"
  }, "A Solutudo movimenta Botucatu"), /*#__PURE__*/React.createElement("div", {
    className: "mov-day"
  }, /*#__PURE__*/React.createElement("span", null, "Hoje")), /*#__PURE__*/React.createElement("div", {
    className: "mov-cols"
  }, /*#__PURE__*/React.createElement("div", {
    className: "mov-col mov-col-l"
  }, left.map((f, i) => /*#__PURE__*/React.createElement(FeedItem, _extends({
    key: i
  }, f)))), /*#__PURE__*/React.createElement("div", {
    className: "mov-line"
  }), /*#__PURE__*/React.createElement("div", {
    className: "mov-col mov-col-r"
  }, right.map((f, i) => /*#__PURE__*/React.createElement(FeedItem, _extends({
    key: i
  }, f))))), /*#__PURE__*/React.createElement("div", {
    className: "mov-day"
  }, /*#__PURE__*/React.createElement("span", null, "Ter\xE7a, 01/01"))));
}
window.Movimento = Movimento;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/consumer-search/movimento.jsx", error: String((e && e.message) || e) }); }

// ui_kits/consumer-search/screens.jsx
try { (() => {
// Consumer Search — screens (window-global Babel module)
const {
  Button,
  Card,
  Badge,
  Avatar,
  StatTile
} = window;
const Ic = window.SolIcons;
const BIZ = [{
  name: "Padaria Pão Quente",
  cat: "Padaria · Confeitaria",
  area: "Centro",
  rating: "4,8",
  open: true,
  tone: "peach"
}, {
  name: "Auto Center Silva",
  cat: "Mecânica · Auto elétrica",
  area: "Vila Assunção",
  rating: "4,6",
  open: true,
  tone: "lavender"
}, {
  name: "Clínica Vida & Saúde",
  cat: "Clínica médica",
  area: "Jardim Paraíso",
  rating: "4,9",
  open: false,
  tone: "mint"
}, {
  name: "Pet Shop Amigo Fiel",
  cat: "Pet shop · Banho e tosa",
  area: "Centro",
  rating: "4,7",
  open: true,
  tone: "yellow"
}, {
  name: "Studio Bella Hair",
  cat: "Salão de beleza",
  area: "Vila Santana",
  rating: "5,0",
  open: true,
  tone: "peach"
}];

/* ---------- Top navigation ---------- */
function TopNav({
  onHome,
  onMov,
  dark
}) {
  const item = (Icon, label, active) => /*#__PURE__*/React.createElement("button", {
    className: "nav-item",
    "data-active": active ? "" : undefined
  }, /*#__PURE__*/React.createElement(Icon, {
    w: 20
  }), " ", /*#__PURE__*/React.createElement("span", null, label));
  return /*#__PURE__*/React.createElement("header", {
    className: "topnav"
  }, /*#__PURE__*/React.createElement("button", {
    className: "logo-btn",
    onClick: onHome
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/logo-solutudo.png",
    alt: "Solutudo"
  })), /*#__PURE__*/React.createElement("nav", {
    className: "nav-center"
  }, item(Ic.Store, "Buscar", true), item(Ic.Briefcase, "Empregos"), item(Ic.Bus, "Ônibus")), /*#__PURE__*/React.createElement("button", {
    className: "user-pill"
  }, /*#__PURE__*/React.createElement(Avatar, {
    src: "../../assets/avatar-b.png",
    name: "U",
    size: 34
  }), /*#__PURE__*/React.createElement(Ic.ChevDown, {
    w: 16
  })));
}

/* ---------- Home / search hero ---------- */
function Home({
  q,
  setQ,
  onSearch,
  onMov,
  onBiz
}) {
  return /*#__PURE__*/React.createElement("div", {
    className: "home"
  }, /*#__PURE__*/React.createElement("div", {
    className: "hero-mesh"
  }), /*#__PURE__*/React.createElement(TopNav, {
    onHome: () => {},
    onMov: onMov
  }), /*#__PURE__*/React.createElement("div", {
    className: "hero-body"
  }, /*#__PURE__*/React.createElement("button", {
    className: "city-switch"
  }, "Mudar ", /*#__PURE__*/React.createElement(Ic.ChevDown, {
    w: 16
  })), /*#__PURE__*/React.createElement("h1", {
    className: "city"
  }, "Botucatu"), /*#__PURE__*/React.createElement("div", {
    className: "searchbar"
  }, /*#__PURE__*/React.createElement("span", {
    className: "sb-ic"
  }, /*#__PURE__*/React.createElement(Ic.Search, {
    w: 26
  })), /*#__PURE__*/React.createElement("input", {
    value: q,
    onChange: e => setQ(e.target.value),
    placeholder: "Busque empresas",
    onKeyDown: e => e.key === "Enter" && onSearch()
  }), /*#__PURE__*/React.createElement("button", {
    className: "sb-mic"
  }, /*#__PURE__*/React.createElement(Ic.Mic, {
    w: 24
  })), /*#__PURE__*/React.createElement("button", {
    className: "sb-go",
    onClick: onSearch
  }, /*#__PURE__*/React.createElement("span", {
    className: "sb-go-t"
  }, "Buscar"), /*#__PURE__*/React.createElement("span", {
    className: "sb-go-h"
  }, "Pressione Enter"))), /*#__PURE__*/React.createElement("div", {
    className: "usage"
  }, /*#__PURE__*/React.createElement("div", {
    className: "usage-avatars"
  }, /*#__PURE__*/React.createElement(Avatar, {
    src: "../../assets/avatar-b.png",
    name: "A",
    size: 40
  }), /*#__PURE__*/React.createElement(Avatar, {
    name: "B",
    size: 40,
    tone: "peach"
  }), /*#__PURE__*/React.createElement(Avatar, {
    name: "C",
    size: 40,
    tone: "mint"
  })), /*#__PURE__*/React.createElement("div", {
    className: "usage-txt"
  }, /*#__PURE__*/React.createElement("b", null, "205.890"), " usam a Solutudo em ", /*#__PURE__*/React.createElement("b", null, "Botucatu"), /*#__PURE__*/React.createElement("button", {
    className: "ver-mov",
    onClick: onMov
  }, "Ver movimento ", /*#__PURE__*/React.createElement(Ic.Arrow, {
    w: 16
  }))))), /*#__PURE__*/React.createElement("div", {
    className: "tiles"
  }, /*#__PURE__*/React.createElement(StatTile, {
    tone: "lavender",
    value: "7.540",
    label: "Empresas cadastradas",
    icon: /*#__PURE__*/React.createElement(Ic.Store, null),
    onClick: onSearch
  }), /*#__PURE__*/React.createElement(StatTile, {
    tone: "mint",
    value: "780",
    label: "Vagas de emprego",
    icon: /*#__PURE__*/React.createElement(Ic.Briefcase, null)
  }), /*#__PURE__*/React.createElement("div", {
    className: "tile-person"
  }, /*#__PURE__*/React.createElement(Avatar, {
    src: "../../assets/avatar-b.png",
    name: "M",
    size: 44
  }), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("b", null, "Fale com Maria"), /*#__PURE__*/React.createElement("span", null, "Assistente Solutudo"))), /*#__PURE__*/React.createElement("div", {
    className: "tile-city"
  }, /*#__PURE__*/React.createElement(Ic.Globe, {
    w: 26
  }), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("b", null, "Conhe\xE7a a cidade"), /*#__PURE__*/React.createElement("span", null, "com a vis\xE3o da Solutudo")))));
}

/* ---------- Search results ---------- */
function Results({
  q,
  onBack,
  onBiz
}) {
  return /*#__PURE__*/React.createElement("div", {
    className: "results"
  }, /*#__PURE__*/React.createElement(TopNav, {
    onHome: onBack
  }), /*#__PURE__*/React.createElement("div", {
    className: "results-body"
  }, /*#__PURE__*/React.createElement("button", {
    className: "back",
    onClick: onBack
  }, /*#__PURE__*/React.createElement(Ic.Arrow, {
    w: 18,
    style: {
      transform: "rotate(180deg)"
    }
  }), " Voltar"), /*#__PURE__*/React.createElement("div", {
    className: "results-head"
  }, /*#__PURE__*/React.createElement("h2", null, "Resultados para ", /*#__PURE__*/React.createElement("span", {
    className: "sol-display sol-gradient-text"
  }, q || "empresas")), /*#__PURE__*/React.createElement("span", {
    className: "results-count"
  }, BIZ.length, " empresas em Botucatu")), /*#__PURE__*/React.createElement("div", {
    className: "results-list"
  }, BIZ.map((b, i) => /*#__PURE__*/React.createElement("button", {
    key: i,
    className: "biz-row",
    onClick: () => onBiz(b)
  }, /*#__PURE__*/React.createElement(Avatar, {
    name: b.name,
    size: 56,
    tone: b.tone
  }), /*#__PURE__*/React.createElement("div", {
    className: "biz-info"
  }, /*#__PURE__*/React.createElement("div", {
    className: "biz-top"
  }, /*#__PURE__*/React.createElement("span", {
    className: "biz-name"
  }, b.name), /*#__PURE__*/React.createElement(Badge, {
    tone: b.open ? "green" : "gray"
  }, b.open ? "Aberto agora" : "Fechado")), /*#__PURE__*/React.createElement("span", {
    className: "biz-cat"
  }, b.cat), /*#__PURE__*/React.createElement("div", {
    className: "biz-meta"
  }, /*#__PURE__*/React.createElement(Badge, {
    tone: "gray",
    iconLeft: /*#__PURE__*/React.createElement(Ic.Pin, null)
  }, b.area), /*#__PURE__*/React.createElement("span", {
    className: "biz-rate"
  }, /*#__PURE__*/React.createElement(Ic.Star, {
    w: 14
  }), " ", b.rating))), /*#__PURE__*/React.createElement(Button, {
    variant: "whatsapp",
    size: "sm",
    iconLeft: /*#__PURE__*/React.createElement(Ic.Whatsapp, {
      w: 16
    })
  }, "WhatsApp"))))));
}

/* ---------- Business profile ---------- */
function Profile({
  biz,
  onBack
}) {
  const b = biz || BIZ[0];
  return /*#__PURE__*/React.createElement("div", {
    className: "profile"
  }, /*#__PURE__*/React.createElement(TopNav, {
    onHome: onBack
  }), /*#__PURE__*/React.createElement("div", {
    className: "profile-body"
  }, /*#__PURE__*/React.createElement("button", {
    className: "back",
    onClick: onBack
  }, /*#__PURE__*/React.createElement(Ic.Arrow, {
    w: 18,
    style: {
      transform: "rotate(180deg)"
    }
  }), " Voltar aos resultados"), /*#__PURE__*/React.createElement(Card, {
    padding: 0,
    radius: "var(--radius-xl)",
    elevation: "md",
    style: {
      overflow: "hidden",
      maxWidth: 460,
      margin: "0 auto"
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "pf-rainbow"
  }), /*#__PURE__*/React.createElement("div", {
    className: "pf-inner"
  }, /*#__PURE__*/React.createElement(Badge, {
    tone: "pink",
    variant: "solid",
    iconLeft: /*#__PURE__*/React.createElement(Ic.Heart, {
      w: 13
    }),
    style: {
      marginBottom: 14
    }
  }, "Recomendada"), /*#__PURE__*/React.createElement(Avatar, {
    name: b.name,
    size: 72,
    tone: b.tone,
    ring: true,
    style: {
      marginBottom: 12
    }
  }), /*#__PURE__*/React.createElement("h2", {
    className: "pf-name"
  }, b.name), /*#__PURE__*/React.createElement("span", {
    className: "pf-cat"
  }, b.cat), /*#__PURE__*/React.createElement("div", {
    className: "pf-rate"
  }, /*#__PURE__*/React.createElement(Ic.Star, {
    w: 16
  }), " ", b.rating, " \xB7 ", /*#__PURE__*/React.createElement("span", null, b.area)), /*#__PURE__*/React.createElement(Button, {
    variant: "whatsapp",
    fullWidth: true,
    iconLeft: /*#__PURE__*/React.createElement(Ic.Whatsapp, {
      w: 18
    }),
    style: {
      marginTop: 18
    }
  }, "Chamar no WhatsApp"), /*#__PURE__*/React.createElement("div", {
    className: "pf-actions"
  }, /*#__PURE__*/React.createElement("button", null, /*#__PURE__*/React.createElement(Ic.Pin, {
    w: 18
  }), " Endere\xE7o"), /*#__PURE__*/React.createElement("button", null, /*#__PURE__*/React.createElement(Ic.Phone, {
    w: 18
  }), " Telefone"), /*#__PURE__*/React.createElement("button", null, /*#__PURE__*/React.createElement(Ic.Globe, {
    w: 18
  }), " Site")), /*#__PURE__*/React.createElement("div", {
    className: "pf-about"
  }, /*#__PURE__*/React.createElement("span", {
    className: "pf-label"
  }, "Sobre a empresa"), /*#__PURE__*/React.createElement("p", null, "Aberto todos os dias das 11h30 at\xE9 o \xFAltimo cliente. Atendimento pr\xF3ximo, produtos selecionados e o melhor da ", b.area, ". Venha conhecer!"))))));
}
window.ConsumerScreens = {
  Home,
  Results,
  Profile,
  TopNav,
  BIZ
};
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/consumer-search/screens.jsx", error: String((e && e.message) || e) }); }

// ui_kits/shared/icons.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
// Solutudo UI-kit shared icons (Lucide-style outline, ~1.8px).
// Window-global Babel module — load with <script type="text/babel">.
const I = ({
  d,
  w = 24,
  s = 1.8,
  fill = "none",
  children,
  ...p
}) => /*#__PURE__*/React.createElement("svg", _extends({
  viewBox: "0 0 24 24",
  width: w,
  height: w,
  fill: fill,
  stroke: fill === "none" ? "currentColor" : "none",
  strokeWidth: s,
  strokeLinecap: "round",
  strokeLinejoin: "round"
}, p), d ? /*#__PURE__*/React.createElement("path", {
  d: d
}) : children);
const Icons = {
  Search: p => /*#__PURE__*/React.createElement(I, p, /*#__PURE__*/React.createElement("circle", {
    cx: "11",
    cy: "11",
    r: "7"
  }), /*#__PURE__*/React.createElement("path", {
    d: "m20 20-3.2-3.2"
  })),
  Mic: p => /*#__PURE__*/React.createElement(I, p, /*#__PURE__*/React.createElement("rect", {
    x: "9",
    y: "2",
    width: "6",
    height: "12",
    rx: "3"
  }), /*#__PURE__*/React.createElement("path", {
    d: "M5 11a7 7 0 0 0 14 0M12 18v3"
  })),
  Store: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    d: "M3 9l1.5-5h15L21 9M4 9v10a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V9M3 9h18"
  })),
  Briefcase: p => /*#__PURE__*/React.createElement(I, p, /*#__PURE__*/React.createElement("rect", {
    x: "3",
    y: "7",
    width: "18",
    height: "13",
    rx: "2"
  }), /*#__PURE__*/React.createElement("path", {
    d: "M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
  })),
  Bus: p => /*#__PURE__*/React.createElement(I, p, /*#__PURE__*/React.createElement("rect", {
    x: "4",
    y: "4",
    width: "16",
    height: "13",
    rx: "2"
  }), /*#__PURE__*/React.createElement("path", {
    d: "M4 11h16M7 20v-3M17 20v-3"
  }), /*#__PURE__*/React.createElement("circle", {
    cx: "8",
    cy: "14",
    r: "0.6",
    fill: "currentColor"
  }), /*#__PURE__*/React.createElement("circle", {
    cx: "16",
    cy: "14",
    r: "0.6",
    fill: "currentColor"
  })),
  Phone: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    d: "M6 3h3l2 5-2 1a12 12 0 0 0 5 5l1-2 5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 4 5a2 2 0 0 1 2-2z"
  })),
  Box: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    d: "m21 8-9-5-9 5 9 5 9-5zM3 8v8l9 5 9-5V8M12 13v8"
  })),
  Pin: p => /*#__PURE__*/React.createElement(I, p, /*#__PURE__*/React.createElement("path", {
    d: "M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11z"
  }), /*#__PURE__*/React.createElement("circle", {
    cx: "12",
    cy: "10",
    r: "2.5"
  })),
  Star: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    fill: "currentColor",
    d: "m12 2 2.9 6.3 6.9.7-5.2 4.6 1.5 6.8L12 17.8 5.9 20.4l1.5-6.8L2.2 9l6.9-.7z"
  })),
  Arrow: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    s: 2.2,
    d: "M5 12h14M13 6l6 6-6 6"
  })),
  ChevDown: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    s: 2.2,
    d: "m6 9 6 6 6-6"
  })),
  Close: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    s: 2.2,
    d: "M6 6l12 12M18 6 6 18"
  })),
  Check: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    s: 3,
    d: "M20 6 9 17l-5-5"
  })),
  Heart: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    d: "M12 21s-7-4.6-9.3-9A5 5 0 0 1 12 6a5 5 0 0 1 9.3 6c-2.3 4.4-9.3 9-9.3 9z"
  })),
  Whatsapp: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    fill: "currentColor",
    d: "M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1-.4-.1-.9-.3-1.6-.6-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8 0-1.3.7-2 .9-2.2.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2.1.4 0 .6l-.4.5c-.2.2-.3.4-.1.7.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.2.1.4.1.6-.1l.7-.9c.2-.2.4-.2.6-.1l1.8.9c.3.1.4.2.5.3.1.2.1.7-.1 1.3Z"
  })),
  Edit: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    d: "M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5z"
  })),
  List: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    d: "M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"
  })),
  Logout: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    d: "M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"
  })),
  Bell: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    d: "M18 8a6 6 0 1 0-12 0c0 7-3 9-3 9h18s-3-2-3-9M13.7 21a2 2 0 0 1-3.4 0"
  })),
  Plus: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    s: 2.2,
    d: "M12 5v14M5 12h14"
  })),
  Chart: p => /*#__PURE__*/React.createElement(I, _extends({}, p, {
    d: "M3 3v18h18M7 15l3-4 3 3 4-6"
  })),
  Globe: p => /*#__PURE__*/React.createElement(I, p, /*#__PURE__*/React.createElement("circle", {
    cx: "12",
    cy: "12",
    r: "9"
  }), /*#__PURE__*/React.createElement("path", {
    d: "M3 12h18M12 3a15 15 0 0 1 0 18 15 15 0 0 1 0-18z"
  }))
};
window.SolIcons = Icons;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/shared/icons.jsx", error: String((e && e.message) || e) }); }

// ui_kits/shared/primitives.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
// Solutudo UI-kit shared primitives — window-global Babel module.
// Mirrors the design-system components (Button, Card, Badge, Avatar,
// StatTile, SearchBar, SegmentedToggle) using the real CSS tokens.

function Button({
  children,
  variant = "primary",
  size = "md",
  iconLeft,
  iconRight,
  fullWidth,
  disabled,
  onClick,
  style = {}
}) {
  const S = {
    sm: {
      f: 13,
      p: "9px 16px",
      g: 7,
      i: 16
    },
    md: {
      f: 15,
      p: "13px 24px",
      g: 9,
      i: 18
    },
    lg: {
      f: 17,
      p: "16px 30px",
      g: 10,
      i: 20
    }
  }[size];
  const V = {
    primary: {
      background: "var(--grad-cta)",
      color: "#fff",
      boxShadow: "var(--shadow-brand)"
    },
    dark: {
      background: "var(--ink)",
      color: "#fff"
    },
    secondary: {
      background: "#fff",
      color: "var(--ink)",
      boxShadow: "var(--ring-hairline)"
    },
    ghost: {
      background: "transparent",
      color: "var(--brand-purple)"
    },
    whatsapp: {
      background: "#25D366",
      color: "#fff"
    }
  }[variant];
  const [h, setH] = React.useState(false),
    [d, setD] = React.useState(false);
  return /*#__PURE__*/React.createElement("button", {
    type: "button",
    disabled: disabled,
    onClick: onClick,
    onMouseEnter: () => setH(true),
    onMouseLeave: () => {
      setH(false);
      setD(false);
    },
    onMouseDown: () => setD(true),
    onMouseUp: () => setD(false),
    style: {
      display: "inline-flex",
      alignItems: "center",
      justifyContent: "center",
      gap: S.g,
      fontFamily: "var(--font-sans)",
      fontWeight: 600,
      fontSize: S.f,
      letterSpacing: "var(--tracking-snug)",
      padding: S.p,
      border: "none",
      borderRadius: "var(--radius-pill)",
      lineHeight: 1,
      whiteSpace: "nowrap",
      cursor: disabled ? "not-allowed" : "pointer",
      width: fullWidth ? "100%" : "auto",
      opacity: disabled ? 0.45 : 1,
      transform: d ? "scale(0.97)" : h && !disabled ? "translateY(-1px)" : "none",
      filter: h && !disabled && variant === "primary" ? "brightness(1.05)" : h && !disabled && variant === "dark" ? "brightness(1.3)" : "none",
      transition: "transform var(--dur-fast) var(--ease-out), filter var(--dur-base) var(--ease-out)",
      ...V,
      ...style
    }
  }, iconLeft && /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      width: S.i,
      height: S.i
    }
  }, iconLeft), children, iconRight && /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      width: S.i,
      height: S.i
    }
  }, iconRight));
}
function Card({
  children,
  padding = 24,
  radius = "var(--radius-xl)",
  elevation = "card",
  tone = "white",
  hairline,
  style = {},
  ...rest
}) {
  const SH = {
    none: "none",
    sm: "var(--shadow-sm)",
    card: "var(--shadow-card)",
    md: "var(--shadow-md)",
    lg: "var(--shadow-lg)"
  };
  const T = {
    white: "#fff",
    sunken: "var(--gray-100)",
    lavender: "var(--tint-lavender)",
    mint: "var(--tint-mint)",
    peach: "var(--tint-peach)",
    yellow: "var(--tint-yellow)"
  };
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      background: T[tone] || tone,
      borderRadius: radius,
      padding,
      boxSizing: "border-box",
      boxShadow: hairline ? "var(--ring-hairline)" : SH[elevation],
      ...style
    }
  }, rest), children);
}
function Badge({
  children,
  tone = "purple",
  variant = "soft",
  iconLeft,
  size = "md",
  style = {}
}) {
  const P = {
    purple: {
      solid: "var(--brand-purple)",
      soft: "var(--tint-lavender)",
      text: "var(--brand-purple)"
    },
    pink: {
      solid: "var(--brand-pink)",
      soft: "var(--tint-pink)",
      text: "var(--brand-pink)"
    },
    orange: {
      solid: "var(--brand-orange)",
      soft: "var(--tint-peach)",
      text: "var(--brand-orange-deep)"
    },
    green: {
      solid: "var(--success)",
      soft: "var(--tint-mint)",
      text: "var(--success)"
    },
    gray: {
      solid: "var(--gray-600)",
      soft: "var(--gray-100)",
      text: "var(--gray-600)"
    },
    dark: {
      solid: "var(--slate-heading)",
      soft: "var(--gray-100)",
      text: "#fff"
    }
  }[tone];
  const S = {
    sm: {
      f: 11,
      p: "3px 9px",
      g: 4,
      i: 12
    },
    md: {
      f: 12.5,
      p: "5px 12px",
      g: 5,
      i: 14
    }
  }[size];
  const ST = {
    soft: {
      background: P.soft,
      color: P.text
    },
    solid: {
      background: P.solid,
      color: "#fff"
    },
    outline: {
      background: "transparent",
      color: P.text,
      boxShadow: `inset 0 0 0 1.3px ${P.solid}`
    }
  }[variant];
  return /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      alignItems: "center",
      gap: S.g,
      fontFamily: "var(--font-sans)",
      fontWeight: 600,
      fontSize: S.f,
      letterSpacing: "var(--tracking-snug)",
      padding: S.p,
      borderRadius: "var(--radius-pill)",
      lineHeight: 1,
      whiteSpace: "nowrap",
      ...ST,
      ...style
    }
  }, iconLeft && /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      width: S.i,
      height: S.i
    }
  }, iconLeft), children);
}
function Avatar({
  src,
  name = "",
  size = 48,
  ring,
  tone = "lavender",
  style = {}
}) {
  const T = {
    lavender: "var(--tint-lavender)",
    mint: "var(--tint-mint)",
    peach: "var(--tint-peach)",
    yellow: "var(--tint-yellow)"
  };
  const inner = /*#__PURE__*/React.createElement("div", {
    style: {
      width: size,
      height: size,
      borderRadius: "50%",
      overflow: "hidden",
      background: T[tone],
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      color: "var(--brand-purple)",
      fontFamily: "var(--font-sans)",
      fontWeight: 700,
      fontSize: size * 0.4,
      flex: "none"
    }
  }, src ? /*#__PURE__*/React.createElement("img", {
    src: src,
    alt: name,
    style: {
      width: "100%",
      height: "100%",
      objectFit: "cover"
    }
  }) : (name || "?").charAt(0).toUpperCase());
  if (!ring) return /*#__PURE__*/React.createElement("div", {
    style: style
  }, inner);
  return /*#__PURE__*/React.createElement("div", {
    style: {
      padding: 2.5,
      borderRadius: "50%",
      background: "var(--grad-brand)",
      display: "inline-flex",
      ...style
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      padding: 2,
      borderRadius: "50%",
      background: "#fff",
      display: "inline-flex"
    }
  }, inner));
}
function StatTile({
  value,
  label,
  icon,
  tone = "lavender",
  onClick,
  style = {}
}) {
  const M = {
    lavender: {
      bg: "var(--tint-lavender)",
      fg: "var(--brand-purple)"
    },
    mint: {
      bg: "var(--tint-mint)",
      fg: "var(--brand-mint)"
    },
    peach: {
      bg: "var(--tint-peach)",
      fg: "var(--brand-orange-deep)"
    },
    yellow: {
      bg: "var(--tint-yellow)",
      fg: "var(--brand-amber)"
    }
  }[tone];
  const [h, setH] = React.useState(false);
  return /*#__PURE__*/React.createElement("div", {
    onClick: onClick,
    onMouseEnter: () => setH(true),
    onMouseLeave: () => setH(false),
    style: {
      background: M.bg,
      borderRadius: "var(--radius-lg)",
      padding: "18px 20px",
      display: "flex",
      alignItems: "center",
      gap: 14,
      cursor: onClick ? "pointer" : "default",
      boxSizing: "border-box",
      transform: h && onClick ? "translateY(-2px)" : "none",
      transition: "transform var(--dur-base) var(--ease-out)",
      ...style
    }
  }, icon && /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      width: 28,
      height: 28,
      color: M.fg,
      flex: "none"
    }
  }, icon), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gap: 2,
      minWidth: 0
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 800,
      fontSize: 24,
      color: "var(--ink)",
      letterSpacing: "var(--tracking-tight)",
      lineHeight: 1
    }
  }, value), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 500,
      fontSize: 13,
      color: "var(--gray-600)",
      letterSpacing: "var(--tracking-snug)",
      overflow: "hidden",
      textOverflow: "ellipsis",
      whiteSpace: "nowrap"
    }
  }, label)));
}
function SegmentedToggle({
  options = [],
  value,
  onChange,
  style = {}
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "inline-flex",
      padding: 4,
      background: "#fff",
      borderRadius: "var(--radius-pill)",
      boxShadow: "var(--ring-hairline)",
      gap: 2,
      ...style
    }
  }, options.map(o => {
    const a = o.value === value;
    return /*#__PURE__*/React.createElement("button", {
      key: o.value,
      type: "button",
      onClick: () => onChange && onChange(o.value),
      style: {
        border: "none",
        cursor: "pointer",
        fontFamily: "var(--font-sans)",
        fontWeight: 600,
        fontSize: 14,
        letterSpacing: "var(--tracking-snug)",
        padding: "9px 22px",
        borderRadius: "var(--radius-pill)",
        background: a ? "var(--brand-purple)" : "transparent",
        color: a ? "#fff" : "var(--gray-500)",
        transition: "all var(--dur-base) var(--ease-out)"
      }
    }, o.label);
  }));
}
function GradientText({
  children,
  style = {}
}) {
  return /*#__PURE__*/React.createElement("span", {
    className: "sol-display sol-gradient-text",
    style: style
  }, children);
}
Object.assign(window, {
  Button,
  Card,
  Badge,
  Avatar,
  StatTile,
  SegmentedToggle,
  GradientText
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/shared/primitives.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Avatar = __ds_scope.Avatar;

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.StatTile = __ds_scope.StatTile;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.SearchBar = __ds_scope.SearchBar;

__ds_ns.SegmentedToggle = __ds_scope.SegmentedToggle;

__ds_ns.FeedItem = __ds_scope.FeedItem;

__ds_ns.PlanCard = __ds_scope.PlanCard;

})();
