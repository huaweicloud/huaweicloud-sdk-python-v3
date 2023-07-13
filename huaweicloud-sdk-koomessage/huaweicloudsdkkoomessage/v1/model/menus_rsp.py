# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MenusRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'menu_id': 'str',
        'pub_id': 'str',
        'pub_name': 'str',
        'logo_img': 'str',
        'logo_url': 'str',
        'menu': 'Menus',
        'menu_state': 'int',
        'approve_state': 'int',
        'online_time': 'str',
        'oper_time': 'str'
    }

    attribute_map = {
        'menu_id': 'menu_id',
        'pub_id': 'pub_id',
        'pub_name': 'pub_name',
        'logo_img': 'logo_img',
        'logo_url': 'logo_url',
        'menu': 'menu',
        'menu_state': 'menu_state',
        'approve_state': 'approve_state',
        'online_time': 'online_time',
        'oper_time': 'oper_time'
    }

    def __init__(self, menu_id=None, pub_id=None, pub_name=None, logo_img=None, logo_url=None, menu=None, menu_state=None, approve_state=None, online_time=None, oper_time=None):
        """MenusRsp

        The model defined in huaweicloud sdk

        :param menu_id: 菜单ID。
        :type menu_id: str
        :param pub_id: 服务号ID。
        :type pub_id: str
        :param pub_name: 服务号名称。
        :type pub_name: str
        :param logo_img: LOGO图片资源ID。
        :type logo_img: str
        :param logo_url: LOGO图片资源URL。
        :type logo_url: str
        :param menu: 
        :type menu: :class:`huaweicloudsdkkoomessage.v1.Menus`
        :param menu_state: 资源状态。  - 1：未生效 - 2：已生效 - 3：已失效  - 4：已冻结  
        :type menu_state: int
        :param approve_state: 审核状态。 - 1：待审核  - 2：通过  - 3：驳回  
        :type approve_state: int
        :param online_time: 上线时间。格式为：2020-12-12T12:00:00Z。
        :type online_time: str
        :param oper_time: 最新操作时间。格式为：2020-12-12T12:00:00Z。
        :type oper_time: str
        """
        
        

        self._menu_id = None
        self._pub_id = None
        self._pub_name = None
        self._logo_img = None
        self._logo_url = None
        self._menu = None
        self._menu_state = None
        self._approve_state = None
        self._online_time = None
        self._oper_time = None
        self.discriminator = None

        if menu_id is not None:
            self.menu_id = menu_id
        if pub_id is not None:
            self.pub_id = pub_id
        if pub_name is not None:
            self.pub_name = pub_name
        if logo_img is not None:
            self.logo_img = logo_img
        if logo_url is not None:
            self.logo_url = logo_url
        if menu is not None:
            self.menu = menu
        if menu_state is not None:
            self.menu_state = menu_state
        if approve_state is not None:
            self.approve_state = approve_state
        if online_time is not None:
            self.online_time = online_time
        if oper_time is not None:
            self.oper_time = oper_time

    @property
    def menu_id(self):
        """Gets the menu_id of this MenusRsp.

        菜单ID。

        :return: The menu_id of this MenusRsp.
        :rtype: str
        """
        return self._menu_id

    @menu_id.setter
    def menu_id(self, menu_id):
        """Sets the menu_id of this MenusRsp.

        菜单ID。

        :param menu_id: The menu_id of this MenusRsp.
        :type menu_id: str
        """
        self._menu_id = menu_id

    @property
    def pub_id(self):
        """Gets the pub_id of this MenusRsp.

        服务号ID。

        :return: The pub_id of this MenusRsp.
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        """Sets the pub_id of this MenusRsp.

        服务号ID。

        :param pub_id: The pub_id of this MenusRsp.
        :type pub_id: str
        """
        self._pub_id = pub_id

    @property
    def pub_name(self):
        """Gets the pub_name of this MenusRsp.

        服务号名称。

        :return: The pub_name of this MenusRsp.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        """Sets the pub_name of this MenusRsp.

        服务号名称。

        :param pub_name: The pub_name of this MenusRsp.
        :type pub_name: str
        """
        self._pub_name = pub_name

    @property
    def logo_img(self):
        """Gets the logo_img of this MenusRsp.

        LOGO图片资源ID。

        :return: The logo_img of this MenusRsp.
        :rtype: str
        """
        return self._logo_img

    @logo_img.setter
    def logo_img(self, logo_img):
        """Sets the logo_img of this MenusRsp.

        LOGO图片资源ID。

        :param logo_img: The logo_img of this MenusRsp.
        :type logo_img: str
        """
        self._logo_img = logo_img

    @property
    def logo_url(self):
        """Gets the logo_url of this MenusRsp.

        LOGO图片资源URL。

        :return: The logo_url of this MenusRsp.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this MenusRsp.

        LOGO图片资源URL。

        :param logo_url: The logo_url of this MenusRsp.
        :type logo_url: str
        """
        self._logo_url = logo_url

    @property
    def menu(self):
        """Gets the menu of this MenusRsp.

        :return: The menu of this MenusRsp.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Menus`
        """
        return self._menu

    @menu.setter
    def menu(self, menu):
        """Sets the menu of this MenusRsp.

        :param menu: The menu of this MenusRsp.
        :type menu: :class:`huaweicloudsdkkoomessage.v1.Menus`
        """
        self._menu = menu

    @property
    def menu_state(self):
        """Gets the menu_state of this MenusRsp.

        资源状态。  - 1：未生效 - 2：已生效 - 3：已失效  - 4：已冻结  

        :return: The menu_state of this MenusRsp.
        :rtype: int
        """
        return self._menu_state

    @menu_state.setter
    def menu_state(self, menu_state):
        """Sets the menu_state of this MenusRsp.

        资源状态。  - 1：未生效 - 2：已生效 - 3：已失效  - 4：已冻结  

        :param menu_state: The menu_state of this MenusRsp.
        :type menu_state: int
        """
        self._menu_state = menu_state

    @property
    def approve_state(self):
        """Gets the approve_state of this MenusRsp.

        审核状态。 - 1：待审核  - 2：通过  - 3：驳回  

        :return: The approve_state of this MenusRsp.
        :rtype: int
        """
        return self._approve_state

    @approve_state.setter
    def approve_state(self, approve_state):
        """Sets the approve_state of this MenusRsp.

        审核状态。 - 1：待审核  - 2：通过  - 3：驳回  

        :param approve_state: The approve_state of this MenusRsp.
        :type approve_state: int
        """
        self._approve_state = approve_state

    @property
    def online_time(self):
        """Gets the online_time of this MenusRsp.

        上线时间。格式为：2020-12-12T12:00:00Z。

        :return: The online_time of this MenusRsp.
        :rtype: str
        """
        return self._online_time

    @online_time.setter
    def online_time(self, online_time):
        """Sets the online_time of this MenusRsp.

        上线时间。格式为：2020-12-12T12:00:00Z。

        :param online_time: The online_time of this MenusRsp.
        :type online_time: str
        """
        self._online_time = online_time

    @property
    def oper_time(self):
        """Gets the oper_time of this MenusRsp.

        最新操作时间。格式为：2020-12-12T12:00:00Z。

        :return: The oper_time of this MenusRsp.
        :rtype: str
        """
        return self._oper_time

    @oper_time.setter
    def oper_time(self, oper_time):
        """Sets the oper_time of this MenusRsp.

        最新操作时间。格式为：2020-12-12T12:00:00Z。

        :param oper_time: The oper_time of this MenusRsp.
        :type oper_time: str
        """
        self._oper_time = oper_time

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
        if not isinstance(other, MenusRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
