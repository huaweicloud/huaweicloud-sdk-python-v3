# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyOttChannelGeneral:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, domain=None, app_name=None, id=None, name=None):
        r"""ModifyOttChannelGeneral

        The model defined in huaweicloud sdk

        :param domain: 频道推流域名
        :type domain: str
        :param app_name: 组名或应用名
        :type app_name: str
        :param id: 频道ID。频道唯一标识，为必填项
        :type id: str
        :param name: 频道名称
        :type name: str
        """
        
        

        self._domain = None
        self._app_name = None
        self._id = None
        self._name = None
        self.discriminator = None

        self.domain = domain
        self.app_name = app_name
        self.id = id
        self.name = name

    @property
    def domain(self):
        r"""Gets the domain of this ModifyOttChannelGeneral.

        频道推流域名

        :return: The domain of this ModifyOttChannelGeneral.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ModifyOttChannelGeneral.

        频道推流域名

        :param domain: The domain of this ModifyOttChannelGeneral.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this ModifyOttChannelGeneral.

        组名或应用名

        :return: The app_name of this ModifyOttChannelGeneral.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ModifyOttChannelGeneral.

        组名或应用名

        :param app_name: The app_name of this ModifyOttChannelGeneral.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this ModifyOttChannelGeneral.

        频道ID。频道唯一标识，为必填项

        :return: The id of this ModifyOttChannelGeneral.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModifyOttChannelGeneral.

        频道ID。频道唯一标识，为必填项

        :param id: The id of this ModifyOttChannelGeneral.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ModifyOttChannelGeneral.

        频道名称

        :return: The name of this ModifyOttChannelGeneral.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModifyOttChannelGeneral.

        频道名称

        :param name: The name of this ModifyOttChannelGeneral.
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
        if not isinstance(other, ModifyOttChannelGeneral):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
