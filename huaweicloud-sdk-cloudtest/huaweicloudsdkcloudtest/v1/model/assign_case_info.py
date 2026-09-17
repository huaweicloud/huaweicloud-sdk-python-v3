# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssignCaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_uri': 'str',
        'is_available': 'bool'
    }

    attribute_map = {
        'case_uri': 'case_uri',
        'is_available': 'is_available'
    }

    def __init__(self, case_uri=None, is_available=None):
        r"""AssignCaseInfo

        The model defined in huaweicloud sdk

        :param case_uri: 用例URI
        :type case_uri: str
        :param is_available: 是否可用
        :type is_available: bool
        """
        
        

        self._case_uri = None
        self._is_available = None
        self.discriminator = None

        if case_uri is not None:
            self.case_uri = case_uri
        if is_available is not None:
            self.is_available = is_available

    @property
    def case_uri(self):
        r"""Gets the case_uri of this AssignCaseInfo.

        用例URI

        :return: The case_uri of this AssignCaseInfo.
        :rtype: str
        """
        return self._case_uri

    @case_uri.setter
    def case_uri(self, case_uri):
        r"""Sets the case_uri of this AssignCaseInfo.

        用例URI

        :param case_uri: The case_uri of this AssignCaseInfo.
        :type case_uri: str
        """
        self._case_uri = case_uri

    @property
    def is_available(self):
        r"""Gets the is_available of this AssignCaseInfo.

        是否可用

        :return: The is_available of this AssignCaseInfo.
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        r"""Sets the is_available of this AssignCaseInfo.

        是否可用

        :param is_available: The is_available of this AssignCaseInfo.
        :type is_available: bool
        """
        self._is_available = is_available

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
        if not isinstance(other, AssignCaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
