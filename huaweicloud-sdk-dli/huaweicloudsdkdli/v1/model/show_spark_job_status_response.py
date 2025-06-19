# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkJobStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state'
    }

    def __init__(self, id=None, state=None):
        r"""ShowSparkJobStatusResponse

        The model defined in huaweicloud sdk

        :param id: 参数解释:  批处理作业的ID，采用UUID（通用唯一识别码）格式 示例: 0a324461-d9d9-45da-a52a-3b3c7a3d809e 约束限制:  无 取值范围: 无 默认取值: 无
        :type id: str
        :param state: 参数解释:  批处理作业的状态。starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复 示例: success 约束限制:  无 取值范围: starting（批处理作业正在启动） running（批处理作业正在执行任务） dead（批处理作业已退出） success（批处理作业执行成功） recovering（批处理作业正在恢复） 默认取值: 无
        :type state: str
        """
        
        super(ShowSparkJobStatusResponse, self).__init__()

        self._id = None
        self._state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state

    @property
    def id(self):
        r"""Gets the id of this ShowSparkJobStatusResponse.

        参数解释:  批处理作业的ID，采用UUID（通用唯一识别码）格式 示例: 0a324461-d9d9-45da-a52a-3b3c7a3d809e 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The id of this ShowSparkJobStatusResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSparkJobStatusResponse.

        参数解释:  批处理作业的ID，采用UUID（通用唯一识别码）格式 示例: 0a324461-d9d9-45da-a52a-3b3c7a3d809e 约束限制:  无 取值范围: 无 默认取值: 无

        :param id: The id of this ShowSparkJobStatusResponse.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this ShowSparkJobStatusResponse.

        参数解释:  批处理作业的状态。starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复 示例: success 约束限制:  无 取值范围: starting（批处理作业正在启动） running（批处理作业正在执行任务） dead（批处理作业已退出） success（批处理作业执行成功） recovering（批处理作业正在恢复） 默认取值: 无

        :return: The state of this ShowSparkJobStatusResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowSparkJobStatusResponse.

        参数解释:  批处理作业的状态。starting：正在启动；running：正在执行任务；dead：session已退出；success：session停止成功；recovering：正在恢复 示例: success 约束限制:  无 取值范围: starting（批处理作业正在启动） running（批处理作业正在执行任务） dead（批处理作业已退出） success（批处理作业执行成功） recovering（批处理作业正在恢复） 默认取值: 无

        :param state: The state of this ShowSparkJobStatusResponse.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, ShowSparkJobStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
