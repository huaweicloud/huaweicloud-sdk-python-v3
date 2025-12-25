# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataObjectRefInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'dict(str, object)',
        'dataclass': 'DataClassRef'
    }

    attribute_map = {
        'content': 'content',
        'dataclass': 'dataclass'
    }

    def __init__(self, content=None, dataclass=None):
        r"""DataObjectRefInfo

        The model defined in huaweicloud sdk

        :param content: 流程实例上下文内容
        :type content: dict(str, object)
        :param dataclass: 
        :type dataclass: :class:`huaweicloudsdksecmaster.v1.DataClassRef`
        """
        
        

        self._content = None
        self._dataclass = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if dataclass is not None:
            self.dataclass = dataclass

    @property
    def content(self):
        r"""Gets the content of this DataObjectRefInfo.

        流程实例上下文内容

        :return: The content of this DataObjectRefInfo.
        :rtype: dict(str, object)
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this DataObjectRefInfo.

        流程实例上下文内容

        :param content: The content of this DataObjectRefInfo.
        :type content: dict(str, object)
        """
        self._content = content

    @property
    def dataclass(self):
        r"""Gets the dataclass of this DataObjectRefInfo.

        :return: The dataclass of this DataObjectRefInfo.
        :rtype: :class:`huaweicloudsdksecmaster.v1.DataClassRef`
        """
        return self._dataclass

    @dataclass.setter
    def dataclass(self, dataclass):
        r"""Sets the dataclass of this DataObjectRefInfo.

        :param dataclass: The dataclass of this DataObjectRefInfo.
        :type dataclass: :class:`huaweicloudsdksecmaster.v1.DataClassRef`
        """
        self._dataclass = dataclass

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
        if not isinstance(other, DataObjectRefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
