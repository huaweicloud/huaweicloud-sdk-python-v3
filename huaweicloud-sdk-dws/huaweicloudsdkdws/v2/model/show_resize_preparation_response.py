# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResizePreparationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'is_support': 'bool',
        'progress': 'str'
    }

    attribute_map = {
        'status': 'status',
        'is_support': 'is_support',
        'progress': 'progress'
    }

    def __init__(self, status=None, is_support=None, progress=None):
        r"""ShowResizePreparationResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释**： 扩容准备的状态。 **取值范围**： INIT：扩容准备初始化中； PREPARING：扩容准备进行中； FAIL：扩容准备失败； SUCCESS：扩容准备成功； WAIT_RETRY：等待扩容准备重试；
        :type status: str
        :param is_support: **参数解释**： 是否支持扩容准备。 **取值范围**： true：支持扩容准备； false：不支持扩容准备；
        :type is_support: bool
        :param progress: **参数解释**： 扩容准备进度。 **取值范围**： 不涉及
        :type progress: str
        """
        
        super().__init__()

        self._status = None
        self._is_support = None
        self._progress = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if is_support is not None:
            self.is_support = is_support
        if progress is not None:
            self.progress = progress

    @property
    def status(self):
        r"""Gets the status of this ShowResizePreparationResponse.

        **参数解释**： 扩容准备的状态。 **取值范围**： INIT：扩容准备初始化中； PREPARING：扩容准备进行中； FAIL：扩容准备失败； SUCCESS：扩容准备成功； WAIT_RETRY：等待扩容准备重试；

        :return: The status of this ShowResizePreparationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowResizePreparationResponse.

        **参数解释**： 扩容准备的状态。 **取值范围**： INIT：扩容准备初始化中； PREPARING：扩容准备进行中； FAIL：扩容准备失败； SUCCESS：扩容准备成功； WAIT_RETRY：等待扩容准备重试；

        :param status: The status of this ShowResizePreparationResponse.
        :type status: str
        """
        self._status = status

    @property
    def is_support(self):
        r"""Gets the is_support of this ShowResizePreparationResponse.

        **参数解释**： 是否支持扩容准备。 **取值范围**： true：支持扩容准备； false：不支持扩容准备；

        :return: The is_support of this ShowResizePreparationResponse.
        :rtype: bool
        """
        return self._is_support

    @is_support.setter
    def is_support(self, is_support):
        r"""Sets the is_support of this ShowResizePreparationResponse.

        **参数解释**： 是否支持扩容准备。 **取值范围**： true：支持扩容准备； false：不支持扩容准备；

        :param is_support: The is_support of this ShowResizePreparationResponse.
        :type is_support: bool
        """
        self._is_support = is_support

    @property
    def progress(self):
        r"""Gets the progress of this ShowResizePreparationResponse.

        **参数解释**： 扩容准备进度。 **取值范围**： 不涉及

        :return: The progress of this ShowResizePreparationResponse.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ShowResizePreparationResponse.

        **参数解释**： 扩容准备进度。 **取值范围**： 不涉及

        :param progress: The progress of this ShowResizePreparationResponse.
        :type progress: str
        """
        self._progress = progress

    def to_dict(self):
        import warnings
        warnings.warn("ShowResizePreparationResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowResizePreparationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
