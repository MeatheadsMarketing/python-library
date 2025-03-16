import tensorrt as trt

def optimize_model_onnx(onnx_model_path, optimized_model_path):
    """Converts an ONNX model to a TensorRT-optimized model."""
    logger = trt.Logger(trt.Logger.WARNING)
    builder = trt.Builder(logger)
    network = builder.create_network()
    parser = trt.OnnxParser(network, logger)

    with open(onnx_model_path, "rb") as f:
        parser.parse(f.read())

    optimized_model = builder.build_cuda_engine(network)
    with open(optimized_model_path, "wb") as f:
        f.write(optimized_model.serialize())
