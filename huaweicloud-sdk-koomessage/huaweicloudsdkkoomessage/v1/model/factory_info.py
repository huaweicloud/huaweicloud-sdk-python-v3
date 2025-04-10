# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FactoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'factory_type': 'str',
        'state': 'int',
        'version': 'str',
        'tpl_id': 'str'
    }

    attribute_map = {
        'factory_type': 'factory_type',
        'state': 'state',
        'version': 'version',
        'tpl_id': 'tpl_id'
    }

    def __init__(self, factory_type=None, state=None, version=None, tpl_id=None):
        r"""FactoryInfo

        The model defined in huaweicloud sdk

        :param factory_type: 厂商类型。  - HUAWEI：表示华为厂商 - XIAOMI：表示小米厂商 - OPPO：表示OPPO厂商 - VIVO：表示VIVO厂商 - MEIZU：表示魅族厂商 - SAMSUNG：表示三星厂商 
        :type factory_type: str
        :param state: 模板状态。  - 1：激活  - 其他：未激活 
        :type state: int
        :param version: 厂商版本
        :type version: str
        :param tpl_id: 智能信息模板ID
        :type tpl_id: str
        """
        
        

        self._factory_type = None
        self._state = None
        self._version = None
        self._tpl_id = None
        self.discriminator = None

        self.factory_type = factory_type
        self.state = state
        if version is not None:
            self.version = version
        if tpl_id is not None:
            self.tpl_id = tpl_id

    @property
    def factory_type(self):
        r"""Gets the factory_type of this FactoryInfo.

        厂商类型。  - HUAWEI：表示华为厂商 - XIAOMI：表示小米厂商 - OPPO：表示OPPO厂商 - VIVO：表示VIVO厂商 - MEIZU：表示魅族厂商 - SAMSUNG：表示三星厂商 

        :return: The factory_type of this FactoryInfo.
        :rtype: str
        """
        return self._factory_type

    @factory_type.setter
    def factory_type(self, factory_type):
        r"""Sets the factory_type of this FactoryInfo.

        厂商类型。  - HUAWEI：表示华为厂商 - XIAOMI：表示小米厂商 - OPPO：表示OPPO厂商 - VIVO：表示VIVO厂商 - MEIZU：表示魅族厂商 - SAMSUNG：表示三星厂商 

        :param factory_type: The factory_type of this FactoryInfo.
        :type factory_type: str
        """
        self._factory_type = factory_type

    @property
    def state(self):
        r"""Gets the state of this FactoryInfo.

        模板状态。  - 1：激活  - 其他：未激活 

        :return: The state of this FactoryInfo.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this FactoryInfo.

        模板状态。  - 1：激活  - 其他：未激活 

        :param state: The state of this FactoryInfo.
        :type state: int
        """
        self._state = state

    @property
    def version(self):
        r"""Gets the version of this FactoryInfo.

        厂商版本

        :return: The version of this FactoryInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this FactoryInfo.

        厂商版本

        :param version: The version of this FactoryInfo.
        :type version: str
        """
        self._version = version

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this FactoryInfo.

        智能信息模板ID

        :return: The tpl_id of this FactoryInfo.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this FactoryInfo.

        智能信息模板ID

        :param tpl_id: The tpl_id of this FactoryInfo.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

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
        if not isinstance(other, FactoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
