# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MockInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mock_id': 'str',
        'mock_switch': 'bool',
        'mock_url': 'str'
    }

    attribute_map = {
        'mock_id': 'mock_id',
        'mock_switch': 'mock_switch',
        'mock_url': 'mock_url'
    }

    def __init__(self, mock_id=None, mock_switch=None, mock_url=None):
        r"""MockInfo

        The model defined in huaweicloud sdk

        :param mock_id: mock id
        :type mock_id: str
        :param mock_switch: mock开关
        :type mock_switch: bool
        :param mock_url: mock url
        :type mock_url: str
        """
        
        

        self._mock_id = None
        self._mock_switch = None
        self._mock_url = None
        self.discriminator = None

        if mock_id is not None:
            self.mock_id = mock_id
        if mock_switch is not None:
            self.mock_switch = mock_switch
        if mock_url is not None:
            self.mock_url = mock_url

    @property
    def mock_id(self):
        r"""Gets the mock_id of this MockInfo.

        mock id

        :return: The mock_id of this MockInfo.
        :rtype: str
        """
        return self._mock_id

    @mock_id.setter
    def mock_id(self, mock_id):
        r"""Sets the mock_id of this MockInfo.

        mock id

        :param mock_id: The mock_id of this MockInfo.
        :type mock_id: str
        """
        self._mock_id = mock_id

    @property
    def mock_switch(self):
        r"""Gets the mock_switch of this MockInfo.

        mock开关

        :return: The mock_switch of this MockInfo.
        :rtype: bool
        """
        return self._mock_switch

    @mock_switch.setter
    def mock_switch(self, mock_switch):
        r"""Sets the mock_switch of this MockInfo.

        mock开关

        :param mock_switch: The mock_switch of this MockInfo.
        :type mock_switch: bool
        """
        self._mock_switch = mock_switch

    @property
    def mock_url(self):
        r"""Gets the mock_url of this MockInfo.

        mock url

        :return: The mock_url of this MockInfo.
        :rtype: str
        """
        return self._mock_url

    @mock_url.setter
    def mock_url(self, mock_url):
        r"""Sets the mock_url of this MockInfo.

        mock url

        :param mock_url: The mock_url of this MockInfo.
        :type mock_url: str
        """
        self._mock_url = mock_url

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
        if not isinstance(other, MockInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
