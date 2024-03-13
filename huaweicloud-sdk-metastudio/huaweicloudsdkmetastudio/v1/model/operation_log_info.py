# coding: utf-8

import six

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
        'operate_user': 'str'
    }

    attribute_map = {
        'operate_time': 'operate_time',
        'log_type': 'log_type',
        'log_description': 'log_description',
        'operate_user': 'operate_user'
    }

    def __init__(self, operate_time=None, log_type=None, log_description=None, operate_user=None):
        """OperationLogInfo

        The model defined in huaweicloud sdk

        :param operate_time: 操作时间,格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”
        :type operate_time: str
        :param log_type: 命令执行结果。 * USER_CREATE_JOD：用户开始分身数字人定制 * USER_VERIFYING_SUBMITTED：用户提交审核 * SYSTEM_VERIFY_FAILED：自动审核失败 * SYSTEM_VERIFY_SUCCESS：自动审核成功 * ADMIN_VERIFY_SUCCESS：人工审核通过 * ADMIN_VERIFY_FAILED：人工审核不通过 * SYSTEM_TRAIN_DATA_PREPROCESSING：训练数据预处理中 * SYSTEM_TRAIN_DATA_PREPROCESS_FAILED：训练数据预处理失败 * SYSTEM_TRAIN_DATA_PREPROCESS_SUCCESS：训练数据预处理成功 * SYSTEM_TRAINING：开始训练 * ADMIN_STOP_TRAIN：人工终止训练 * SYSTEM_TRAIN_FAILED：训练失败 * SYSTEM_TRAIN_SUCCESS：训练成功 * SYSTEM_INFERENCE_DATA_PREPROCESSING：推理数据预处理中 * SYSTEM_INFERENCE_DATA_PREPROCESS_FAILED：推理数据预处理失败 * SYSTEM_INFERENCE_DATA_PREPROCESS_SUCCESS：推理数据预处理成功 * SYSTEM_JOB_SUCCESS：任务处理完成 * SYSTEM_MARKABLE_VIDEO: 标定视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO: 校验视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO_SUCCESS：校验视频生成成功 * SYSTEM_MASK_VERIFY_VIDEO_FAILED：校验视频生成失败 * SYSTEM_MARKABLE_VIDEO_SUCCESS：标定视频生成成功 * SYSTEM_MARKABLE_VIDEO_FAILED：标定视频生成失败 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_SUCCESS：自动标定成功 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_FAILED：自动标定失败 * ADMIN_MASK_UPLOADED：遮罩文件上传完成 * ADMIN_UPDATE_VIDEO：管理员更换视频 * USER_UPDATE_VIDEO：用户更换视频 * ADMIN_MASK_ACTION_TIME：管理员标定
        :type log_type: str
        :param log_description: 日志描述。用于记录人工审核不通过时的审核意见和DHTS、DHPS上报的错误信息。
        :type log_description: str
        :param operate_user: 操作人员。 * USER：用户 * ADMIN：管理员 * SYSTEM：系统
        :type operate_user: str
        """
        
        

        self._operate_time = None
        self._log_type = None
        self._log_description = None
        self._operate_user = None
        self.discriminator = None

        if operate_time is not None:
            self.operate_time = operate_time
        if log_type is not None:
            self.log_type = log_type
        if log_description is not None:
            self.log_description = log_description
        if operate_user is not None:
            self.operate_user = operate_user

    @property
    def operate_time(self):
        """Gets the operate_time of this OperationLogInfo.

        操作时间,格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :return: The operate_time of this OperationLogInfo.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this OperationLogInfo.

        操作时间,格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :param operate_time: The operate_time of this OperationLogInfo.
        :type operate_time: str
        """
        self._operate_time = operate_time

    @property
    def log_type(self):
        """Gets the log_type of this OperationLogInfo.

        命令执行结果。 * USER_CREATE_JOD：用户开始分身数字人定制 * USER_VERIFYING_SUBMITTED：用户提交审核 * SYSTEM_VERIFY_FAILED：自动审核失败 * SYSTEM_VERIFY_SUCCESS：自动审核成功 * ADMIN_VERIFY_SUCCESS：人工审核通过 * ADMIN_VERIFY_FAILED：人工审核不通过 * SYSTEM_TRAIN_DATA_PREPROCESSING：训练数据预处理中 * SYSTEM_TRAIN_DATA_PREPROCESS_FAILED：训练数据预处理失败 * SYSTEM_TRAIN_DATA_PREPROCESS_SUCCESS：训练数据预处理成功 * SYSTEM_TRAINING：开始训练 * ADMIN_STOP_TRAIN：人工终止训练 * SYSTEM_TRAIN_FAILED：训练失败 * SYSTEM_TRAIN_SUCCESS：训练成功 * SYSTEM_INFERENCE_DATA_PREPROCESSING：推理数据预处理中 * SYSTEM_INFERENCE_DATA_PREPROCESS_FAILED：推理数据预处理失败 * SYSTEM_INFERENCE_DATA_PREPROCESS_SUCCESS：推理数据预处理成功 * SYSTEM_JOB_SUCCESS：任务处理完成 * SYSTEM_MARKABLE_VIDEO: 标定视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO: 校验视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO_SUCCESS：校验视频生成成功 * SYSTEM_MASK_VERIFY_VIDEO_FAILED：校验视频生成失败 * SYSTEM_MARKABLE_VIDEO_SUCCESS：标定视频生成成功 * SYSTEM_MARKABLE_VIDEO_FAILED：标定视频生成失败 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_SUCCESS：自动标定成功 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_FAILED：自动标定失败 * ADMIN_MASK_UPLOADED：遮罩文件上传完成 * ADMIN_UPDATE_VIDEO：管理员更换视频 * USER_UPDATE_VIDEO：用户更换视频 * ADMIN_MASK_ACTION_TIME：管理员标定

        :return: The log_type of this OperationLogInfo.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this OperationLogInfo.

        命令执行结果。 * USER_CREATE_JOD：用户开始分身数字人定制 * USER_VERIFYING_SUBMITTED：用户提交审核 * SYSTEM_VERIFY_FAILED：自动审核失败 * SYSTEM_VERIFY_SUCCESS：自动审核成功 * ADMIN_VERIFY_SUCCESS：人工审核通过 * ADMIN_VERIFY_FAILED：人工审核不通过 * SYSTEM_TRAIN_DATA_PREPROCESSING：训练数据预处理中 * SYSTEM_TRAIN_DATA_PREPROCESS_FAILED：训练数据预处理失败 * SYSTEM_TRAIN_DATA_PREPROCESS_SUCCESS：训练数据预处理成功 * SYSTEM_TRAINING：开始训练 * ADMIN_STOP_TRAIN：人工终止训练 * SYSTEM_TRAIN_FAILED：训练失败 * SYSTEM_TRAIN_SUCCESS：训练成功 * SYSTEM_INFERENCE_DATA_PREPROCESSING：推理数据预处理中 * SYSTEM_INFERENCE_DATA_PREPROCESS_FAILED：推理数据预处理失败 * SYSTEM_INFERENCE_DATA_PREPROCESS_SUCCESS：推理数据预处理成功 * SYSTEM_JOB_SUCCESS：任务处理完成 * SYSTEM_MARKABLE_VIDEO: 标定视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO: 校验视频生成任务 * SYSTEM_MASK_VERIFY_VIDEO_SUCCESS：校验视频生成成功 * SYSTEM_MASK_VERIFY_VIDEO_FAILED：校验视频生成失败 * SYSTEM_MARKABLE_VIDEO_SUCCESS：标定视频生成成功 * SYSTEM_MARKABLE_VIDEO_FAILED：标定视频生成失败 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_SUCCESS：自动标定成功 * SYSTEM_MASK_VIDEO_AND_ACTION_TIME_FAILED：自动标定失败 * ADMIN_MASK_UPLOADED：遮罩文件上传完成 * ADMIN_UPDATE_VIDEO：管理员更换视频 * USER_UPDATE_VIDEO：用户更换视频 * ADMIN_MASK_ACTION_TIME：管理员标定

        :param log_type: The log_type of this OperationLogInfo.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def log_description(self):
        """Gets the log_description of this OperationLogInfo.

        日志描述。用于记录人工审核不通过时的审核意见和DHTS、DHPS上报的错误信息。

        :return: The log_description of this OperationLogInfo.
        :rtype: str
        """
        return self._log_description

    @log_description.setter
    def log_description(self, log_description):
        """Sets the log_description of this OperationLogInfo.

        日志描述。用于记录人工审核不通过时的审核意见和DHTS、DHPS上报的错误信息。

        :param log_description: The log_description of this OperationLogInfo.
        :type log_description: str
        """
        self._log_description = log_description

    @property
    def operate_user(self):
        """Gets the operate_user of this OperationLogInfo.

        操作人员。 * USER：用户 * ADMIN：管理员 * SYSTEM：系统

        :return: The operate_user of this OperationLogInfo.
        :rtype: str
        """
        return self._operate_user

    @operate_user.setter
    def operate_user(self, operate_user):
        """Sets the operate_user of this OperationLogInfo.

        操作人员。 * USER：用户 * ADMIN：管理员 * SYSTEM：系统

        :param operate_user: The operate_user of this OperationLogInfo.
        :type operate_user: str
        """
        self._operate_user = operate_user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
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
