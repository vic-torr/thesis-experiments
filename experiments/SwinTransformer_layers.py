[SwinTransformer(
   (features): Sequential(
     (0): Sequential(
       (0): Conv2d(3, 96, kernel_size=(4, 4), stride=(4, 4))
       (1): Permute()
       (2): LayerNorm((96,), eps=1e-05, elementwise_affine=True)
     )
     (1): Sequential(
       (0): SwinTransformerBlock(
         (norm1): LayerNorm((96,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=96, out_features=288, bias=True)
           (proj): Linear(in_features=96, out_features=96, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.0, mode=row)
         (norm2): LayerNorm((96,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=96, out_features=384, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=384, out_features=96, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
       (1): SwinTransformerBlock(
         (norm1): LayerNorm((96,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=96, out_features=288, bias=True)
           (proj): Linear(in_features=96, out_features=96, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.018181818181818184, mode=row)
         (norm2): LayerNorm((96,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=96, out_features=384, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=384, out_features=96, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
     )
     (2): PatchMerging(
       (reduction): Linear(in_features=384, out_features=192, bias=False)
       (norm): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
     )
     (3): Sequential(
       (0): SwinTransformerBlock(
         (norm1): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=192, out_features=576, bias=True)
           (proj): Linear(in_features=192, out_features=192, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.03636363636363637, mode=row)
         (norm2): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=192, out_features=768, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=768, out_features=192, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
       (1): SwinTransformerBlock(
         (norm1): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=192, out_features=576, bias=True)
           (proj): Linear(in_features=192, out_features=192, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.05454545454545456, mode=row)
         (norm2): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=192, out_features=768, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=768, out_features=192, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
     )
     (4): PatchMerging(
       (reduction): Linear(in_features=768, out_features=384, bias=False)
       (norm): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
     )
     (5): Sequential(
       (0): SwinTransformerBlock(
         (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=384, out_features=1152, bias=True)
           (proj): Linear(in_features=384, out_features=384, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.07272727272727274, mode=row)
         (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=384, out_features=1536, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=1536, out_features=384, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
       (1): SwinTransformerBlock(
         (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=384, out_features=1152, bias=True)
           (proj): Linear(in_features=384, out_features=384, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.09090909090909091, mode=row)
         (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=384, out_features=1536, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=1536, out_features=384, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
       (2): SwinTransformerBlock(
         (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=384, out_features=1152, bias=True)
           (proj): Linear(in_features=384, out_features=384, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.10909090909090911, mode=row)
         (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=384, out_features=1536, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=1536, out_features=384, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
       (3): SwinTransformerBlock(
         (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=384, out_features=1152, bias=True)
           (proj): Linear(in_features=384, out_features=384, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.1272727272727273, mode=row)
         (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=384, out_features=1536, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=1536, out_features=384, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
       (4): SwinTransformerBlock(
         (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=384, out_features=1152, bias=True)
           (proj): Linear(in_features=384, out_features=384, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.14545454545454548, mode=row)
         (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=384, out_features=1536, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=1536, out_features=384, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
       (5): SwinTransformerBlock(
         (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=384, out_features=1152, bias=True)
           (proj): Linear(in_features=384, out_features=384, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.16363636363636364, mode=row)
         (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=384, out_features=1536, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=1536, out_features=384, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
     )
     (6): PatchMerging(
       (reduction): Linear(in_features=1536, out_features=768, bias=False)
       (norm): LayerNorm((1536,), eps=1e-05, elementwise_affine=True)
     )
     (7): Sequential(
       (0): SwinTransformerBlock(
         (norm1): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=768, out_features=2304, bias=True)
           (proj): Linear(in_features=768, out_features=768, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.18181818181818182, mode=row)
         (norm2): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=768, out_features=3072, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=3072, out_features=768, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
       (1): SwinTransformerBlock(
         (norm1): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
         (attn): ShiftedWindowAttention(
           (qkv): Linear(in_features=768, out_features=2304, bias=True)
           (proj): Linear(in_features=768, out_features=768, bias=True)
         )
         (stochastic_depth): StochasticDepth(p=0.2, mode=row)
         (norm2): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
         (mlp): MLP(
           (0): Linear(in_features=768, out_features=3072, bias=True)
           (1): GELU(approximate=none)
           (2): Dropout(p=0.0, inplace=False)
           (3): Linear(in_features=3072, out_features=768, bias=True)
           (4): Dropout(p=0.0, inplace=False)
         )
       )
     )
   )
   (norm): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
   (avgpool): AdaptiveAvgPool2d(output_size=1)
   (head): Linear(in_features=768, out_features=1000, bias=True)
 ),
 Conv2d(3, 96, kernel_size=(4, 4), stride=(4, 4)),
 Permute(),
 LayerNorm((96,), eps=1e-05, elementwise_affine=True),
 SwinTransformerBlock(
   (norm1): LayerNorm((96,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=96, out_features=288, bias=True)
     (proj): Linear(in_features=96, out_features=96, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.0, mode=row)
   (norm2): LayerNorm((96,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=96, out_features=384, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=384, out_features=96, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((96,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=96, out_features=288, bias=True)
   (proj): Linear(in_features=96, out_features=96, bias=True)
 ),
 Linear(in_features=96, out_features=288, bias=True),
 Linear(in_features=96, out_features=96, bias=True),
 StochasticDepth(p=0.0, mode=row),
 LayerNorm((96,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=96, out_features=384, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=384, out_features=96, bias=True),
 Dropout(p=0.0, inplace=False),
 SwinTransformerBlock(
   (norm1): LayerNorm((96,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=96, out_features=288, bias=True)
     (proj): Linear(in_features=96, out_features=96, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.018181818181818184, mode=row)
   (norm2): LayerNorm((96,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=96, out_features=384, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=384, out_features=96, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((96,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=96, out_features=288, bias=True)
   (proj): Linear(in_features=96, out_features=96, bias=True)
 ),
 Linear(in_features=96, out_features=288, bias=True),
 Linear(in_features=96, out_features=96, bias=True),
 StochasticDepth(p=0.018181818181818184, mode=row),
 LayerNorm((96,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=96, out_features=384, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=384, out_features=96, bias=True),
 Dropout(p=0.0, inplace=False),
 PatchMerging(
   (reduction): Linear(in_features=384, out_features=192, bias=False)
   (norm): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
 ),
 Linear(in_features=384, out_features=192, bias=False),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 SwinTransformerBlock(
   (norm1): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=192, out_features=576, bias=True)
     (proj): Linear(in_features=192, out_features=192, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.03636363636363637, mode=row)
   (norm2): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=192, out_features=768, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=768, out_features=192, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((192,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=192, out_features=576, bias=True)
   (proj): Linear(in_features=192, out_features=192, bias=True)
 ),
 Linear(in_features=192, out_features=576, bias=True),
 Linear(in_features=192, out_features=192, bias=True),
 StochasticDepth(p=0.03636363636363637, mode=row),
 LayerNorm((192,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=192, out_features=768, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=768, out_features=192, bias=True),
 Dropout(p=0.0, inplace=False),
 SwinTransformerBlock(
   (norm1): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=192, out_features=576, bias=True)
     (proj): Linear(in_features=192, out_features=192, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.05454545454545456, mode=row)
   (norm2): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=192, out_features=768, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=768, out_features=192, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((192,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=192, out_features=576, bias=True)
   (proj): Linear(in_features=192, out_features=192, bias=True)
 ),
 Linear(in_features=192, out_features=576, bias=True),
 Linear(in_features=192, out_features=192, bias=True),
 StochasticDepth(p=0.05454545454545456, mode=row),
 LayerNorm((192,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=192, out_features=768, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=768, out_features=192, bias=True),
 Dropout(p=0.0, inplace=False),
 PatchMerging(
   (reduction): Linear(in_features=768, out_features=384, bias=False)
   (norm): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
 ),
 Linear(in_features=768, out_features=384, bias=False),
 LayerNorm((768,), eps=1e-05, elementwise_affine=True),
 SwinTransformerBlock(
   (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=384, out_features=1152, bias=True)
     (proj): Linear(in_features=384, out_features=384, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.07272727272727274, mode=row)
   (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=384, out_features=1536, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=1536, out_features=384, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=384, out_features=1152, bias=True)
   (proj): Linear(in_features=384, out_features=384, bias=True)
 ),
 Linear(in_features=384, out_features=1152, bias=True),
 Linear(in_features=384, out_features=384, bias=True),
 StochasticDepth(p=0.07272727272727274, mode=row),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=384, out_features=1536, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=1536, out_features=384, bias=True),
 Dropout(p=0.0, inplace=False),
 SwinTransformerBlock(
   (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=384, out_features=1152, bias=True)
     (proj): Linear(in_features=384, out_features=384, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.09090909090909091, mode=row)
   (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=384, out_features=1536, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=1536, out_features=384, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=384, out_features=1152, bias=True)
   (proj): Linear(in_features=384, out_features=384, bias=True)
 ),
 Linear(in_features=384, out_features=1152, bias=True),
 Linear(in_features=384, out_features=384, bias=True),
 StochasticDepth(p=0.09090909090909091, mode=row),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=384, out_features=1536, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=1536, out_features=384, bias=True),
 Dropout(p=0.0, inplace=False),
 SwinTransformerBlock(
   (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=384, out_features=1152, bias=True)
     (proj): Linear(in_features=384, out_features=384, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.10909090909090911, mode=row)
   (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=384, out_features=1536, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=1536, out_features=384, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=384, out_features=1152, bias=True)
   (proj): Linear(in_features=384, out_features=384, bias=True)
 ),
 Linear(in_features=384, out_features=1152, bias=True),
 Linear(in_features=384, out_features=384, bias=True),
 StochasticDepth(p=0.10909090909090911, mode=row),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=384, out_features=1536, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=1536, out_features=384, bias=True),
 Dropout(p=0.0, inplace=False),
 SwinTransformerBlock(
   (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=384, out_features=1152, bias=True)
     (proj): Linear(in_features=384, out_features=384, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.1272727272727273, mode=row)
   (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=384, out_features=1536, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=1536, out_features=384, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=384, out_features=1152, bias=True)
   (proj): Linear(in_features=384, out_features=384, bias=True)
 ),
 Linear(in_features=384, out_features=1152, bias=True),
 Linear(in_features=384, out_features=384, bias=True),
 StochasticDepth(p=0.1272727272727273, mode=row),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=384, out_features=1536, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=1536, out_features=384, bias=True),
 Dropout(p=0.0, inplace=False),
 SwinTransformerBlock(
   (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=384, out_features=1152, bias=True)
     (proj): Linear(in_features=384, out_features=384, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.14545454545454548, mode=row)
   (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=384, out_features=1536, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=1536, out_features=384, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=384, out_features=1152, bias=True)
   (proj): Linear(in_features=384, out_features=384, bias=True)
 ),
 Linear(in_features=384, out_features=1152, bias=True),
 Linear(in_features=384, out_features=384, bias=True),
 StochasticDepth(p=0.14545454545454548, mode=row),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=384, out_features=1536, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=1536, out_features=384, bias=True),
 Dropout(p=0.0, inplace=False),
 SwinTransformerBlock(
   (norm1): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=384, out_features=1152, bias=True)
     (proj): Linear(in_features=384, out_features=384, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.16363636363636364, mode=row)
   (norm2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=384, out_features=1536, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=1536, out_features=384, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=384, out_features=1152, bias=True)
   (proj): Linear(in_features=384, out_features=384, bias=True)
 ),
 Linear(in_features=384, out_features=1152, bias=True),
 Linear(in_features=384, out_features=384, bias=True),
 StochasticDepth(p=0.16363636363636364, mode=row),
 LayerNorm((384,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=384, out_features=1536, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=1536, out_features=384, bias=True),
 Dropout(p=0.0, inplace=False),
 PatchMerging(
   (reduction): Linear(in_features=1536, out_features=768, bias=False)
   (norm): LayerNorm((1536,), eps=1e-05, elementwise_affine=True)
 ),
 Linear(in_features=1536, out_features=768, bias=False),
 LayerNorm((1536,), eps=1e-05, elementwise_affine=True),
 SwinTransformerBlock(
   (norm1): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=768, out_features=2304, bias=True)
     (proj): Linear(in_features=768, out_features=768, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.18181818181818182, mode=row)
   (norm2): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=768, out_features=3072, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=3072, out_features=768, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((768,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=768, out_features=2304, bias=True)
   (proj): Linear(in_features=768, out_features=768, bias=True)
 ),
 Linear(in_features=768, out_features=2304, bias=True),
 Linear(in_features=768, out_features=768, bias=True),
 StochasticDepth(p=0.18181818181818182, mode=row),
 LayerNorm((768,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=768, out_features=3072, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=3072, out_features=768, bias=True),
 Dropout(p=0.0, inplace=False),
 SwinTransformerBlock(
   (norm1): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
   (attn): ShiftedWindowAttention(
     (qkv): Linear(in_features=768, out_features=2304, bias=True)
     (proj): Linear(in_features=768, out_features=768, bias=True)
   )
   (stochastic_depth): StochasticDepth(p=0.2, mode=row)
   (norm2): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
   (mlp): MLP(
     (0): Linear(in_features=768, out_features=3072, bias=True)
     (1): GELU(approximate=none)
     (2): Dropout(p=0.0, inplace=False)
     (3): Linear(in_features=3072, out_features=768, bias=True)
     (4): Dropout(p=0.0, inplace=False)
   )
 ),
 LayerNorm((768,), eps=1e-05, elementwise_affine=True),
 ShiftedWindowAttention(
   (qkv): Linear(in_features=768, out_features=2304, bias=True)
   (proj): Linear(in_features=768, out_features=768, bias=True)
 ),
 Linear(in_features=768, out_features=2304, bias=True),
 Linear(in_features=768, out_features=768, bias=True),
 StochasticDepth(p=0.2, mode=row),
 LayerNorm((768,), eps=1e-05, elementwise_affine=True),
 Linear(in_features=768, out_features=3072, bias=True),
 GELU(approximate=none),
 Dropout(p=0.0, inplace=False),
 Linear(in_features=3072, out_features=768, bias=True),
 Dropout(p=0.0, inplace=False),
 LayerNorm((768,), eps=1e-05, elementwise_affine=True),
 AdaptiveAvgPool2d(output_size=1),
 Linear(in_features=768, out_features=1000, bias=True)]