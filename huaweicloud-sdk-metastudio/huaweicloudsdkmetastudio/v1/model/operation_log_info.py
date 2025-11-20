# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationLogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_time': 'str',
        'log_type': 'str',
        'log_description': 'str',
        'operate_user': 'str',
        'error_code': 'str',
        'redo_reasons': 'list[str]'
    }

    attribute_map = {
        'operate_time': 'operate_time',
        'log_type': 'log_type',
        'log_description': 'log_description',
        'operate_user': 'operate_user',
        'error_code': 'error_code',
        'redo_reasons': 'redo_reasons'
    }

    def __init__(self, operate_time=None, log_type=None, log_description=None, operate_user=None, error_code=None, redo_reasons=None):
        r"""OperationLogInfo

        The model defined in huaweicloud sdk

        :param operate_time: 操作时间,格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”
        :type operate_time: str
        :param log_type: 命令执行结果。 * USER_CREATE_JOD：用户开始分身数字人定制 * USER_VERIFYING_SUBMITTED：用户提交审核 * SYSTEM_VERIFY_FAILED：自动审核失败 * ADMIN_UPDATE_BEAUTY_LEVEL：管理员更新美白等级 * ADMIN_UPDATE_JOB_PRIORITY：管理员更新任务等级 * SYSTEM_VERIFY_SUCCESS：自动审核成功 * ADMIN_VERIFY_SUCCESS：人工审核通过 * ADMIN_VERIFY_FAILED：人工审核不通过 * SYSTEM_TRAIN_DATA_PREPROCESSING：训练数据预处理中 * SYSTEM_TRAIN_DATA_PREPROCESS_FAILED：训练数据预处理失败 * SYSTEM_TRAIN_DATA_PREPROCESS_SUCCESS：训练数据预处理成功 * SYSTEM_ACTION_GENERATE_DATA_PREPROCESSING：动作编排原子动作生成中 * SYSTEM_ACTION_GENERATE_DATA_SUCCESS：动作编排原子动作生成成功 * SYSTEM_ACTION_GENERATE_ORI_SUCCESS：动作编排资产数据生成成功 * SYSTEM_ACTION_GENERATE_DATA_FAILED：动作编排原子动作生成失败 * SYSTEM_ACTION_GENERATE_ORI_FAILED：动作编排资产数据生成失败 * SYSTEM_ACTION_GENERATE_ORI_PREPROCESSING：动作编排资产数据生成中 * SYSTEM_TRAINING：开始训练 * ADMIN_STOP_TRAINING_DATA_PREPROCESS：人工中止训练 * ADMIN_STOP_BEAUTY_PREPROCESS：人工中止美白 * ADMIN_STOP_INFERENCE_DATA_PREPROCESS：人工中止推理预处理 * ADMIN_STOP_TRAIN：人工终止训练 * SYSTEM_TRAIN_FAILED：训练失败 * SYSTEM_TRAIN_SUCCESS：训练成功 * SYSTEM_INFERENCE_DATA_PREPROCESSING：推理数据预处理中 * SYSTEM_INFERENCE_DATA_PREPROCESS_FAILED：推理数据预处理失败 * SYSTEM_INFERENCE_DATA_PREPROCESS_SUCCESS：推理数据预处理成功 * SYSTEM_JOB_SUCCESS：任务处理完成 * ADMIN_MASK_UPLOADED：遮罩文件上传完成（已废弃） * ADMIN_UPDATE_VIDEO：管理员更换视频 * ADMIN_UPDATE_ACTION_VIDEO：管理员更换动作编排视频 * ADMIN_RESET：管理员一键重置 * ADMIN_ACCEPT：管理员通过 * USER_REPAIR：用户修复 * SYSTEM_UPDATE_COVER：更换封面 * SYSTEM_ANALYSE_FILE_INFO：系统解析文件信息 * ADMIN_SET_SILENCE_REPEAT_NUM：管理员设置静默轮数 * SYSTEM_MARKABLE_VIDEO：标记视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO：校验视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO_SUCCESS：校验视频生成成功 * SYSTEM_MASK_VERIFY_VIDEO_FAILED：校验视频生成失败 * SYSTEM_MARKABLE_VIDEO_SUCCESS：标记视频生成成功 * SYSTEM_BEAUTY_PREPROCESSING：美白处理中 * SYSTEM_BEAUTY_PREPROCESS_FAILED：美白处理失败 * ADMIN_CONFIRM_ACTION：管理员确认动作 * ADMIN_STOP_ACTION_GENERATE_DATA_PREPROCESS：人工中止原子动作生成 * ADMIN_STOP_ACTION_GENERATE_ORI_PREPROCESS：人工中止动作编排 * SYSTEM_BEAUTY_PREPROCESS_SUCCESS：美白视频训练预处理成功 * SYSTEM_COMPILE_FAILED：转编译失败 * SYSTEM_COMPILE_SUCCESS：转编译成功 * SYSTEM_MARKABLE_VIDEO_FAILED：标记视频生成失败 * ADMIN_UPDATE_COMPILE：管理员更新转编译配置 * ADMIN_UPDATE_INFERENCE_DATA_PROCESS_VIDEO：管理员更新推理预处理时间段信息 * SYSTEM_EXECUTE_COMPILE：执行转编译 * SYSTEM_EXECUTE_BEAUTY：执行美白处理 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_SUCCESS：自动标记成功 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_FAILED：自动标记失败 * USER_UPDATE_VIDEO：用户更换视频 * ADMIN_UPLOAD_JSON_DATA：管理员上传动作数据 * ADMIN_DELETE_JSON_DATA：管理员删除动作数据 * ADMIN_UPDATE_GENERAL_CONFIG：管理员更新通用配置 * ADMIN_MASK_ACTION_TIME：管理员标记 * STOP_COMPILE：人工中止转编译 * MAKE_TEST_VIDEO：测试视频 * ADMIN_SET_FLEXUS_RETRY_COUNT：管理员设置flexus任务重试次数 * USER_DELETE_JOB_VIDEO：用户删除任务相关视频 * ADMIN_SET_VIDEO_ROTATION_ANGLE：管理员设置视频旋转角度 * ADMIN_RE_SET_VIDEO_ROTATION_ANGLE：管理员恢复视频旋转角度 * SYSTEM_SET_VIDEO_ROTATION_ANGLE_SUCCESS：视频旋转成功 * SYSTEM_SET_VIDEO_ROTATION_ANGLE_FAILED：视频旋转失败 * COMPILE_JOB_IS_CONSUME：转编译任务被消费 * RESTART_TEST_VIDEO_CHECK: 重新执行测试视频检测 * SKIP_TEST_VIDEO_CHECK:跳过测试视频检测 * WAIT_TEST_VIDEO_CHECK:等待测试视频检测 * TEST_VIDEO_CHECK_PROCESSING:测试视频检测中 * TEST_VIDEO_CHECK_SUCCESS:测试视频检测成功 * TEST_VIDEO_CHECK_FAILED:测试视频检测失败 * REDO_INFERENCE_PREPROCESSING：重新预处理推理数据 * REDO_TRAINING_PREPROCESSING：重新预处理训练数据 * REDO_TRAINING：重新训练 * REDO_ACTION_DATA_GENERATE：重新生成原子动作 * REDO_ACTION_ORI_GENERATE：重新动作编排 * VIDEO_ANALYZE_PROCESSING：视频检测中 * VIDEO_ANALYZE_SUCCESS：视频检测通过 * VIDEO_ANALYZE_FAILED：视频检测未通过 * ADMIN_RESOLUTION_NORMALIZE：管理员分辨率归一化 * SYSTEM_SET_RESOLUTION_NORMALIZE_SUCCESS：管理员分辨率归一化成功 * SYSTEM_SET_RESOLUTION_NORMALIZE_FAILED：管理员分辨率归一化失败 * SYSTEM_ACTION_MARK_PREPROCESS_FAILED 动作标定任务失败 * SYSTEM_ACTION_MARK_PREPROCESSING：动作标定任务生成中 * SYSTEM_ACTION_MARK_PREPROCESS_SUCCESS：动作标定任务成功 * REDO_ACTION_MARK：重新生成原子动作标记 * CONFIRM_ACTION_MARK：确定预标记原子动作 * MANUL_STOP_ACTION_MARK：中止动作标定 * TIME_OUT_RETRY：超时重试
        :type log_type: str
        :param log_description: 日志描述。用于记录人工或自动审核不通过时的审核意见。
        :type log_description: str
        :param operate_user: 操作人员。 * USER：用户 * ADMIN：管理员 * SYSTEM：系统
        :type operate_user: str
        :param error_code: 系统自动驳回时的错误码： * 44005901：视频分辨率不符合要求，目前只接受 1080p(1920x1080, 1080x1920) 或 4K(3840x2160, 2160x3840) 这四种分辨率
        :type error_code: str
        :param redo_reasons: 任务被管理员重新执行的问题原因列表。
        :type redo_reasons: list[str]
        """
        
        

        self._operate_time = None
        self._log_type = None
        self._log_description = None
        self._operate_user = None
        self._error_code = None
        self._redo_reasons = None
        self.discriminator = None

        if operate_time is not None:
            self.operate_time = operate_time
        if log_type is not None:
            self.log_type = log_type
        if log_description is not None:
            self.log_description = log_description
        if operate_user is not None:
            self.operate_user = operate_user
        if error_code is not None:
            self.error_code = error_code
        if redo_reasons is not None:
            self.redo_reasons = redo_reasons

    @property
    def operate_time(self):
        r"""Gets the operate_time of this OperationLogInfo.

        操作时间,格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :return: The operate_time of this OperationLogInfo.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        r"""Sets the operate_time of this OperationLogInfo.

        操作时间,格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :param operate_time: The operate_time of this OperationLogInfo.
        :type operate_time: str
        """
        self._operate_time = operate_time

    @property
    def log_type(self):
        r"""Gets the log_type of this OperationLogInfo.

        命令执行结果。 * USER_CREATE_JOD：用户开始分身数字人定制 * USER_VERIFYING_SUBMITTED：用户提交审核 * SYSTEM_VERIFY_FAILED：自动审核失败 * ADMIN_UPDATE_BEAUTY_LEVEL：管理员更新美白等级 * ADMIN_UPDATE_JOB_PRIORITY：管理员更新任务等级 * SYSTEM_VERIFY_SUCCESS：自动审核成功 * ADMIN_VERIFY_SUCCESS：人工审核通过 * ADMIN_VERIFY_FAILED：人工审核不通过 * SYSTEM_TRAIN_DATA_PREPROCESSING：训练数据预处理中 * SYSTEM_TRAIN_DATA_PREPROCESS_FAILED：训练数据预处理失败 * SYSTEM_TRAIN_DATA_PREPROCESS_SUCCESS：训练数据预处理成功 * SYSTEM_ACTION_GENERATE_DATA_PREPROCESSING：动作编排原子动作生成中 * SYSTEM_ACTION_GENERATE_DATA_SUCCESS：动作编排原子动作生成成功 * SYSTEM_ACTION_GENERATE_ORI_SUCCESS：动作编排资产数据生成成功 * SYSTEM_ACTION_GENERATE_DATA_FAILED：动作编排原子动作生成失败 * SYSTEM_ACTION_GENERATE_ORI_FAILED：动作编排资产数据生成失败 * SYSTEM_ACTION_GENERATE_ORI_PREPROCESSING：动作编排资产数据生成中 * SYSTEM_TRAINING：开始训练 * ADMIN_STOP_TRAINING_DATA_PREPROCESS：人工中止训练 * ADMIN_STOP_BEAUTY_PREPROCESS：人工中止美白 * ADMIN_STOP_INFERENCE_DATA_PREPROCESS：人工中止推理预处理 * ADMIN_STOP_TRAIN：人工终止训练 * SYSTEM_TRAIN_FAILED：训练失败 * SYSTEM_TRAIN_SUCCESS：训练成功 * SYSTEM_INFERENCE_DATA_PREPROCESSING：推理数据预处理中 * SYSTEM_INFERENCE_DATA_PREPROCESS_FAILED：推理数据预处理失败 * SYSTEM_INFERENCE_DATA_PREPROCESS_SUCCESS：推理数据预处理成功 * SYSTEM_JOB_SUCCESS：任务处理完成 * ADMIN_MASK_UPLOADED：遮罩文件上传完成（已废弃） * ADMIN_UPDATE_VIDEO：管理员更换视频 * ADMIN_UPDATE_ACTION_VIDEO：管理员更换动作编排视频 * ADMIN_RESET：管理员一键重置 * ADMIN_ACCEPT：管理员通过 * USER_REPAIR：用户修复 * SYSTEM_UPDATE_COVER：更换封面 * SYSTEM_ANALYSE_FILE_INFO：系统解析文件信息 * ADMIN_SET_SILENCE_REPEAT_NUM：管理员设置静默轮数 * SYSTEM_MARKABLE_VIDEO：标记视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO：校验视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO_SUCCESS：校验视频生成成功 * SYSTEM_MASK_VERIFY_VIDEO_FAILED：校验视频生成失败 * SYSTEM_MARKABLE_VIDEO_SUCCESS：标记视频生成成功 * SYSTEM_BEAUTY_PREPROCESSING：美白处理中 * SYSTEM_BEAUTY_PREPROCESS_FAILED：美白处理失败 * ADMIN_CONFIRM_ACTION：管理员确认动作 * ADMIN_STOP_ACTION_GENERATE_DATA_PREPROCESS：人工中止原子动作生成 * ADMIN_STOP_ACTION_GENERATE_ORI_PREPROCESS：人工中止动作编排 * SYSTEM_BEAUTY_PREPROCESS_SUCCESS：美白视频训练预处理成功 * SYSTEM_COMPILE_FAILED：转编译失败 * SYSTEM_COMPILE_SUCCESS：转编译成功 * SYSTEM_MARKABLE_VIDEO_FAILED：标记视频生成失败 * ADMIN_UPDATE_COMPILE：管理员更新转编译配置 * ADMIN_UPDATE_INFERENCE_DATA_PROCESS_VIDEO：管理员更新推理预处理时间段信息 * SYSTEM_EXECUTE_COMPILE：执行转编译 * SYSTEM_EXECUTE_BEAUTY：执行美白处理 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_SUCCESS：自动标记成功 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_FAILED：自动标记失败 * USER_UPDATE_VIDEO：用户更换视频 * ADMIN_UPLOAD_JSON_DATA：管理员上传动作数据 * ADMIN_DELETE_JSON_DATA：管理员删除动作数据 * ADMIN_UPDATE_GENERAL_CONFIG：管理员更新通用配置 * ADMIN_MASK_ACTION_TIME：管理员标记 * STOP_COMPILE：人工中止转编译 * MAKE_TEST_VIDEO：测试视频 * ADMIN_SET_FLEXUS_RETRY_COUNT：管理员设置flexus任务重试次数 * USER_DELETE_JOB_VIDEO：用户删除任务相关视频 * ADMIN_SET_VIDEO_ROTATION_ANGLE：管理员设置视频旋转角度 * ADMIN_RE_SET_VIDEO_ROTATION_ANGLE：管理员恢复视频旋转角度 * SYSTEM_SET_VIDEO_ROTATION_ANGLE_SUCCESS：视频旋转成功 * SYSTEM_SET_VIDEO_ROTATION_ANGLE_FAILED：视频旋转失败 * COMPILE_JOB_IS_CONSUME：转编译任务被消费 * RESTART_TEST_VIDEO_CHECK: 重新执行测试视频检测 * SKIP_TEST_VIDEO_CHECK:跳过测试视频检测 * WAIT_TEST_VIDEO_CHECK:等待测试视频检测 * TEST_VIDEO_CHECK_PROCESSING:测试视频检测中 * TEST_VIDEO_CHECK_SUCCESS:测试视频检测成功 * TEST_VIDEO_CHECK_FAILED:测试视频检测失败 * REDO_INFERENCE_PREPROCESSING：重新预处理推理数据 * REDO_TRAINING_PREPROCESSING：重新预处理训练数据 * REDO_TRAINING：重新训练 * REDO_ACTION_DATA_GENERATE：重新生成原子动作 * REDO_ACTION_ORI_GENERATE：重新动作编排 * VIDEO_ANALYZE_PROCESSING：视频检测中 * VIDEO_ANALYZE_SUCCESS：视频检测通过 * VIDEO_ANALYZE_FAILED：视频检测未通过 * ADMIN_RESOLUTION_NORMALIZE：管理员分辨率归一化 * SYSTEM_SET_RESOLUTION_NORMALIZE_SUCCESS：管理员分辨率归一化成功 * SYSTEM_SET_RESOLUTION_NORMALIZE_FAILED：管理员分辨率归一化失败 * SYSTEM_ACTION_MARK_PREPROCESS_FAILED 动作标定任务失败 * SYSTEM_ACTION_MARK_PREPROCESSING：动作标定任务生成中 * SYSTEM_ACTION_MARK_PREPROCESS_SUCCESS：动作标定任务成功 * REDO_ACTION_MARK：重新生成原子动作标记 * CONFIRM_ACTION_MARK：确定预标记原子动作 * MANUL_STOP_ACTION_MARK：中止动作标定 * TIME_OUT_RETRY：超时重试

        :return: The log_type of this OperationLogInfo.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this OperationLogInfo.

        命令执行结果。 * USER_CREATE_JOD：用户开始分身数字人定制 * USER_VERIFYING_SUBMITTED：用户提交审核 * SYSTEM_VERIFY_FAILED：自动审核失败 * ADMIN_UPDATE_BEAUTY_LEVEL：管理员更新美白等级 * ADMIN_UPDATE_JOB_PRIORITY：管理员更新任务等级 * SYSTEM_VERIFY_SUCCESS：自动审核成功 * ADMIN_VERIFY_SUCCESS：人工审核通过 * ADMIN_VERIFY_FAILED：人工审核不通过 * SYSTEM_TRAIN_DATA_PREPROCESSING：训练数据预处理中 * SYSTEM_TRAIN_DATA_PREPROCESS_FAILED：训练数据预处理失败 * SYSTEM_TRAIN_DATA_PREPROCESS_SUCCESS：训练数据预处理成功 * SYSTEM_ACTION_GENERATE_DATA_PREPROCESSING：动作编排原子动作生成中 * SYSTEM_ACTION_GENERATE_DATA_SUCCESS：动作编排原子动作生成成功 * SYSTEM_ACTION_GENERATE_ORI_SUCCESS：动作编排资产数据生成成功 * SYSTEM_ACTION_GENERATE_DATA_FAILED：动作编排原子动作生成失败 * SYSTEM_ACTION_GENERATE_ORI_FAILED：动作编排资产数据生成失败 * SYSTEM_ACTION_GENERATE_ORI_PREPROCESSING：动作编排资产数据生成中 * SYSTEM_TRAINING：开始训练 * ADMIN_STOP_TRAINING_DATA_PREPROCESS：人工中止训练 * ADMIN_STOP_BEAUTY_PREPROCESS：人工中止美白 * ADMIN_STOP_INFERENCE_DATA_PREPROCESS：人工中止推理预处理 * ADMIN_STOP_TRAIN：人工终止训练 * SYSTEM_TRAIN_FAILED：训练失败 * SYSTEM_TRAIN_SUCCESS：训练成功 * SYSTEM_INFERENCE_DATA_PREPROCESSING：推理数据预处理中 * SYSTEM_INFERENCE_DATA_PREPROCESS_FAILED：推理数据预处理失败 * SYSTEM_INFERENCE_DATA_PREPROCESS_SUCCESS：推理数据预处理成功 * SYSTEM_JOB_SUCCESS：任务处理完成 * ADMIN_MASK_UPLOADED：遮罩文件上传完成（已废弃） * ADMIN_UPDATE_VIDEO：管理员更换视频 * ADMIN_UPDATE_ACTION_VIDEO：管理员更换动作编排视频 * ADMIN_RESET：管理员一键重置 * ADMIN_ACCEPT：管理员通过 * USER_REPAIR：用户修复 * SYSTEM_UPDATE_COVER：更换封面 * SYSTEM_ANALYSE_FILE_INFO：系统解析文件信息 * ADMIN_SET_SILENCE_REPEAT_NUM：管理员设置静默轮数 * SYSTEM_MARKABLE_VIDEO：标记视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO：校验视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO_SUCCESS：校验视频生成成功 * SYSTEM_MASK_VERIFY_VIDEO_FAILED：校验视频生成失败 * SYSTEM_MARKABLE_VIDEO_SUCCESS：标记视频生成成功 * SYSTEM_BEAUTY_PREPROCESSING：美白处理中 * SYSTEM_BEAUTY_PREPROCESS_FAILED：美白处理失败 * ADMIN_CONFIRM_ACTION：管理员确认动作 * ADMIN_STOP_ACTION_GENERATE_DATA_PREPROCESS：人工中止原子动作生成 * ADMIN_STOP_ACTION_GENERATE_ORI_PREPROCESS：人工中止动作编排 * SYSTEM_BEAUTY_PREPROCESS_SUCCESS：美白视频训练预处理成功 * SYSTEM_COMPILE_FAILED：转编译失败 * SYSTEM_COMPILE_SUCCESS：转编译成功 * SYSTEM_MARKABLE_VIDEO_FAILED：标记视频生成失败 * ADMIN_UPDATE_COMPILE：管理员更新转编译配置 * ADMIN_UPDATE_INFERENCE_DATA_PROCESS_VIDEO：管理员更新推理预处理时间段信息 * SYSTEM_EXECUTE_COMPILE：执行转编译 * SYSTEM_EXECUTE_BEAUTY：执行美白处理 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_SUCCESS：自动标记成功 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_FAILED：自动标记失败 * USER_UPDATE_VIDEO：用户更换视频 * ADMIN_UPLOAD_JSON_DATA：管理员上传动作数据 * ADMIN_DELETE_JSON_DATA：管理员删除动作数据 * ADMIN_UPDATE_GENERAL_CONFIG：管理员更新通用配置 * ADMIN_MASK_ACTION_TIME：管理员标记 * STOP_COMPILE：人工中止转编译 * MAKE_TEST_VIDEO：测试视频 * ADMIN_SET_FLEXUS_RETRY_COUNT：管理员设置flexus任务重试次数 * USER_DELETE_JOB_VIDEO：用户删除任务相关视频 * ADMIN_SET_VIDEO_ROTATION_ANGLE：管理员设置视频旋转角度 * ADMIN_RE_SET_VIDEO_ROTATION_ANGLE：管理员恢复视频旋转角度 * SYSTEM_SET_VIDEO_ROTATION_ANGLE_SUCCESS：视频旋转成功 * SYSTEM_SET_VIDEO_ROTATION_ANGLE_FAILED：视频旋转失败 * COMPILE_JOB_IS_CONSUME：转编译任务被消费 * RESTART_TEST_VIDEO_CHECK: 重新执行测试视频检测 * SKIP_TEST_VIDEO_CHECK:跳过测试视频检测 * WAIT_TEST_VIDEO_CHECK:等待测试视频检测 * TEST_VIDEO_CHECK_PROCESSING:测试视频检测中 * TEST_VIDEO_CHECK_SUCCESS:测试视频检测成功 * TEST_VIDEO_CHECK_FAILED:测试视频检测失败 * REDO_INFERENCE_PREPROCESSING：重新预处理推理数据 * REDO_TRAINING_PREPROCESSING：重新预处理训练数据 * REDO_TRAINING：重新训练 * REDO_ACTION_DATA_GENERATE：重新生成原子动作 * REDO_ACTION_ORI_GENERATE：重新动作编排 * VIDEO_ANALYZE_PROCESSING：视频检测中 * VIDEO_ANALYZE_SUCCESS：视频检测通过 * VIDEO_ANALYZE_FAILED：视频检测未通过 * ADMIN_RESOLUTION_NORMALIZE：管理员分辨率归一化 * SYSTEM_SET_RESOLUTION_NORMALIZE_SUCCESS：管理员分辨率归一化成功 * SYSTEM_SET_RESOLUTION_NORMALIZE_FAILED：管理员分辨率归一化失败 * SYSTEM_ACTION_MARK_PREPROCESS_FAILED 动作标定任务失败 * SYSTEM_ACTION_MARK_PREPROCESSING：动作标定任务生成中 * SYSTEM_ACTION_MARK_PREPROCESS_SUCCESS：动作标定任务成功 * REDO_ACTION_MARK：重新生成原子动作标记 * CONFIRM_ACTION_MARK：确定预标记原子动作 * MANUL_STOP_ACTION_MARK：中止动作标定 * TIME_OUT_RETRY：超时重试

        :param log_type: The log_type of this OperationLogInfo.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def log_description(self):
        r"""Gets the log_description of this OperationLogInfo.

        日志描述。用于记录人工或自动审核不通过时的审核意见。

        :return: The log_description of this OperationLogInfo.
        :rtype: str
        """
        return self._log_description

    @log_description.setter
    def log_description(self, log_description):
        r"""Sets the log_description of this OperationLogInfo.

        日志描述。用于记录人工或自动审核不通过时的审核意见。

        :param log_description: The log_description of this OperationLogInfo.
        :type log_description: str
        """
        self._log_description = log_description

    @property
    def operate_user(self):
        r"""Gets the operate_user of this OperationLogInfo.

        操作人员。 * USER：用户 * ADMIN：管理员 * SYSTEM：系统

        :return: The operate_user of this OperationLogInfo.
        :rtype: str
        """
        return self._operate_user

    @operate_user.setter
    def operate_user(self, operate_user):
        r"""Sets the operate_user of this OperationLogInfo.

        操作人员。 * USER：用户 * ADMIN：管理员 * SYSTEM：系统

        :param operate_user: The operate_user of this OperationLogInfo.
        :type operate_user: str
        """
        self._operate_user = operate_user

    @property
    def error_code(self):
        r"""Gets the error_code of this OperationLogInfo.

        系统自动驳回时的错误码： * 44005901：视频分辨率不符合要求，目前只接受 1080p(1920x1080, 1080x1920) 或 4K(3840x2160, 2160x3840) 这四种分辨率

        :return: The error_code of this OperationLogInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this OperationLogInfo.

        系统自动驳回时的错误码： * 44005901：视频分辨率不符合要求，目前只接受 1080p(1920x1080, 1080x1920) 或 4K(3840x2160, 2160x3840) 这四种分辨率

        :param error_code: The error_code of this OperationLogInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def redo_reasons(self):
        r"""Gets the redo_reasons of this OperationLogInfo.

        任务被管理员重新执行的问题原因列表。

        :return: The redo_reasons of this OperationLogInfo.
        :rtype: list[str]
        """
        return self._redo_reasons

    @redo_reasons.setter
    def redo_reasons(self, redo_reasons):
        r"""Sets the redo_reasons of this OperationLogInfo.

        任务被管理员重新执行的问题原因列表。

        :param redo_reasons: The redo_reasons of this OperationLogInfo.
        :type redo_reasons: list[str]
        """
        self._redo_reasons = redo_reasons

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OperationLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
