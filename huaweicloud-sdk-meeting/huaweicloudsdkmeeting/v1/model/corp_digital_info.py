# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CorpDigitalInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account': 'str',
        'corp_id': 'str',
        'type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'account': 'account',
        'corp_id': 'corpId',
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, account=None, corp_id=None, type=None, name=None):
        """CorpDigitalInfo

        The model defined in huaweicloud sdk

        :param account: 音色资产标识ID。
        :type account: str
        :param corp_id: 当前会议企业ID。
        :type corp_id: str
        :param type: 类型，PUBLIC：公共、LOCAL：本地会议、PRIVATE：克隆专用。
        :type type: str
        :param name: 音色名称。
        :type name: str
        """
        
        

        self._account = None
        self._corp_id = None
        self._type = None
        self._name = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if corp_id is not None:
            self.corp_id = corp_id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name

    @property
    def account(self):
        """Gets the account of this CorpDigitalInfo.

        音色资产标识ID。

        :return: The account of this CorpDigitalInfo.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this CorpDigitalInfo.

        音色资产标识ID。

        :param account: The account of this CorpDigitalInfo.
        :type account: str
        """
        self._account = account

    @property
    def corp_id(self):
        """Gets the corp_id of this CorpDigitalInfo.

        当前会议企业ID。

        :return: The corp_id of this CorpDigitalInfo.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        """Sets the corp_id of this CorpDigitalInfo.

        当前会议企业ID。

        :param corp_id: The corp_id of this CorpDigitalInfo.
        :type corp_id: str
        """
        self._corp_id = corp_id

    @property
    def type(self):
        """Gets the type of this CorpDigitalInfo.

        类型，PUBLIC：公共、LOCAL：本地会议、PRIVATE：克隆专用。

        :return: The type of this CorpDigitalInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CorpDigitalInfo.

        类型，PUBLIC：公共、LOCAL：本地会议、PRIVATE：克隆专用。

        :param type: The type of this CorpDigitalInfo.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this CorpDigitalInfo.

        音色名称。

        :return: The name of this CorpDigitalInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CorpDigitalInfo.

        音色名称。

        :param name: The name of this CorpDigitalInfo.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CorpDigitalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
