# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePubInfoResponseModelData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_id': 'str',
        'pub_id': 'str',
        'menu_id': 'str',
        'portal_id': 'str',
        'pub_name': 'str'
    }

    attribute_map = {
        'log_id': 'log_id',
        'pub_id': 'pub_id',
        'menu_id': 'menu_id',
        'portal_id': 'portal_id',
        'pub_name': 'pub_name'
    }

    def __init__(self, log_id=None, pub_id=None, menu_id=None, portal_id=None, pub_name=None):
        r"""CreatePubInfoResponseModelData

        The model defined in huaweicloud sdk

        :param log_id: 服务号申请记录ID。
        :type log_id: str
        :param pub_id: 服务号ID。
        :type pub_id: str
        :param menu_id: 菜单ID。
        :type menu_id: str
        :param portal_id: 主页ID。
        :type portal_id: str
        :param pub_name: 服务号名称。
        :type pub_name: str
        """
        
        

        self._log_id = None
        self._pub_id = None
        self._menu_id = None
        self._portal_id = None
        self._pub_name = None
        self.discriminator = None

        self.log_id = log_id
        if pub_id is not None:
            self.pub_id = pub_id
        if menu_id is not None:
            self.menu_id = menu_id
        if portal_id is not None:
            self.portal_id = portal_id
        if pub_name is not None:
            self.pub_name = pub_name

    @property
    def log_id(self):
        r"""Gets the log_id of this CreatePubInfoResponseModelData.

        服务号申请记录ID。

        :return: The log_id of this CreatePubInfoResponseModelData.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        r"""Sets the log_id of this CreatePubInfoResponseModelData.

        服务号申请记录ID。

        :param log_id: The log_id of this CreatePubInfoResponseModelData.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def pub_id(self):
        r"""Gets the pub_id of this CreatePubInfoResponseModelData.

        服务号ID。

        :return: The pub_id of this CreatePubInfoResponseModelData.
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        r"""Sets the pub_id of this CreatePubInfoResponseModelData.

        服务号ID。

        :param pub_id: The pub_id of this CreatePubInfoResponseModelData.
        :type pub_id: str
        """
        self._pub_id = pub_id

    @property
    def menu_id(self):
        r"""Gets the menu_id of this CreatePubInfoResponseModelData.

        菜单ID。

        :return: The menu_id of this CreatePubInfoResponseModelData.
        :rtype: str
        """
        return self._menu_id

    @menu_id.setter
    def menu_id(self, menu_id):
        r"""Sets the menu_id of this CreatePubInfoResponseModelData.

        菜单ID。

        :param menu_id: The menu_id of this CreatePubInfoResponseModelData.
        :type menu_id: str
        """
        self._menu_id = menu_id

    @property
    def portal_id(self):
        r"""Gets the portal_id of this CreatePubInfoResponseModelData.

        主页ID。

        :return: The portal_id of this CreatePubInfoResponseModelData.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        r"""Sets the portal_id of this CreatePubInfoResponseModelData.

        主页ID。

        :param portal_id: The portal_id of this CreatePubInfoResponseModelData.
        :type portal_id: str
        """
        self._portal_id = portal_id

    @property
    def pub_name(self):
        r"""Gets the pub_name of this CreatePubInfoResponseModelData.

        服务号名称。

        :return: The pub_name of this CreatePubInfoResponseModelData.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        r"""Sets the pub_name of this CreatePubInfoResponseModelData.

        服务号名称。

        :param pub_name: The pub_name of this CreatePubInfoResponseModelData.
        :type pub_name: str
        """
        self._pub_name = pub_name

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
        if not isinstance(other, CreatePubInfoResponseModelData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
