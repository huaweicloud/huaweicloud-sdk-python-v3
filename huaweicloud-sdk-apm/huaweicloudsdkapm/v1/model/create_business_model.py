# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBusinessModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'eps_id': 'str',
        'display_name': 'str',
        'descp': 'str',
        'cmdb_datasource_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'eps_id': 'eps_id',
        'display_name': 'display_name',
        'descp': 'descp',
        'cmdb_datasource_type': 'cmdb_datasource_type'
    }

    def __init__(self, name=None, eps_id=None, display_name=None, descp=None, cmdb_datasource_type=None):
        r"""CreateBusinessModel

        The model defined in huaweicloud sdk

        :param name: 应用名字
        :type name: str
        :param eps_id: 企业项目ID，默认值为“0”，表示默认项目的ID。
        :type eps_id: str
        :param display_name: CMDB树显示的名称
        :type display_name: str
        :param descp: 描述
        :type descp: str
        :param cmdb_datasource_type: 默认值为SKYWALKING。
        :type cmdb_datasource_type: str
        """
        
        

        self._name = None
        self._eps_id = None
        self._display_name = None
        self._descp = None
        self._cmdb_datasource_type = None
        self.discriminator = None

        self.name = name
        if eps_id is not None:
            self.eps_id = eps_id
        self.display_name = display_name
        self.descp = descp
        if cmdb_datasource_type is not None:
            self.cmdb_datasource_type = cmdb_datasource_type

    @property
    def name(self):
        r"""Gets the name of this CreateBusinessModel.

        应用名字

        :return: The name of this CreateBusinessModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateBusinessModel.

        应用名字

        :param name: The name of this CreateBusinessModel.
        :type name: str
        """
        self._name = name

    @property
    def eps_id(self):
        r"""Gets the eps_id of this CreateBusinessModel.

        企业项目ID，默认值为“0”，表示默认项目的ID。

        :return: The eps_id of this CreateBusinessModel.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this CreateBusinessModel.

        企业项目ID，默认值为“0”，表示默认项目的ID。

        :param eps_id: The eps_id of this CreateBusinessModel.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def display_name(self):
        r"""Gets the display_name of this CreateBusinessModel.

        CMDB树显示的名称

        :return: The display_name of this CreateBusinessModel.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CreateBusinessModel.

        CMDB树显示的名称

        :param display_name: The display_name of this CreateBusinessModel.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def descp(self):
        r"""Gets the descp of this CreateBusinessModel.

        描述

        :return: The descp of this CreateBusinessModel.
        :rtype: str
        """
        return self._descp

    @descp.setter
    def descp(self, descp):
        r"""Sets the descp of this CreateBusinessModel.

        描述

        :param descp: The descp of this CreateBusinessModel.
        :type descp: str
        """
        self._descp = descp

    @property
    def cmdb_datasource_type(self):
        r"""Gets the cmdb_datasource_type of this CreateBusinessModel.

        默认值为SKYWALKING。

        :return: The cmdb_datasource_type of this CreateBusinessModel.
        :rtype: str
        """
        return self._cmdb_datasource_type

    @cmdb_datasource_type.setter
    def cmdb_datasource_type(self, cmdb_datasource_type):
        r"""Sets the cmdb_datasource_type of this CreateBusinessModel.

        默认值为SKYWALKING。

        :param cmdb_datasource_type: The cmdb_datasource_type of this CreateBusinessModel.
        :type cmdb_datasource_type: str
        """
        self._cmdb_datasource_type = cmdb_datasource_type

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
        if not isinstance(other, CreateBusinessModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
