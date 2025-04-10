# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsAppAddReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'create_sign_and_template': 'bool',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'region': 'str',
        'up_link_addr': 'str',
        'show_secret': 'bool'
    }

    attribute_map = {
        'app_name': 'app_name',
        'create_sign_and_template': 'create_sign_and_template',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'region': 'region',
        'up_link_addr': 'up_link_addr',
        'show_secret': 'show_secret'
    }

    def __init__(self, app_name=None, create_sign_and_template=None, enterprise_project_id=None, enterprise_project_name=None, region=None, up_link_addr=None, show_secret=None):
        r"""SmsAppAddReq

        The model defined in huaweicloud sdk

        :param app_name: 应用名称
        :type app_name: str
        :param create_sign_and_template: 是否创建测试签名和模板。只有地域为国内时，该字段有效 true：是 false：否
        :type create_sign_and_template: bool
        :param enterprise_project_id: 企业项目ID，默认为0
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称，默认为default
        :type enterprise_project_name: str
        :param region: 地域 1. cn：国内 2. intl：国际
        :type region: str
        :param up_link_addr: 上行回调地址。只有地域为国内时，
        :type up_link_addr: str
        :param show_secret: 是否在返回体中显示app_secret字段
        :type show_secret: bool
        """
        
        

        self._app_name = None
        self._create_sign_and_template = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._region = None
        self._up_link_addr = None
        self._show_secret = None
        self.discriminator = None

        self.app_name = app_name
        if create_sign_and_template is not None:
            self.create_sign_and_template = create_sign_and_template
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        self.region = region
        if up_link_addr is not None:
            self.up_link_addr = up_link_addr
        if show_secret is not None:
            self.show_secret = show_secret

    @property
    def app_name(self):
        r"""Gets the app_name of this SmsAppAddReq.

        应用名称

        :return: The app_name of this SmsAppAddReq.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this SmsAppAddReq.

        应用名称

        :param app_name: The app_name of this SmsAppAddReq.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def create_sign_and_template(self):
        r"""Gets the create_sign_and_template of this SmsAppAddReq.

        是否创建测试签名和模板。只有地域为国内时，该字段有效 true：是 false：否

        :return: The create_sign_and_template of this SmsAppAddReq.
        :rtype: bool
        """
        return self._create_sign_and_template

    @create_sign_and_template.setter
    def create_sign_and_template(self, create_sign_and_template):
        r"""Sets the create_sign_and_template of this SmsAppAddReq.

        是否创建测试签名和模板。只有地域为国内时，该字段有效 true：是 false：否

        :param create_sign_and_template: The create_sign_and_template of this SmsAppAddReq.
        :type create_sign_and_template: bool
        """
        self._create_sign_and_template = create_sign_and_template

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SmsAppAddReq.

        企业项目ID，默认为0

        :return: The enterprise_project_id of this SmsAppAddReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SmsAppAddReq.

        企业项目ID，默认为0

        :param enterprise_project_id: The enterprise_project_id of this SmsAppAddReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this SmsAppAddReq.

        企业项目名称，默认为default

        :return: The enterprise_project_name of this SmsAppAddReq.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this SmsAppAddReq.

        企业项目名称，默认为default

        :param enterprise_project_name: The enterprise_project_name of this SmsAppAddReq.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def region(self):
        r"""Gets the region of this SmsAppAddReq.

        地域 1. cn：国内 2. intl：国际

        :return: The region of this SmsAppAddReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this SmsAppAddReq.

        地域 1. cn：国内 2. intl：国际

        :param region: The region of this SmsAppAddReq.
        :type region: str
        """
        self._region = region

    @property
    def up_link_addr(self):
        r"""Gets the up_link_addr of this SmsAppAddReq.

        上行回调地址。只有地域为国内时，

        :return: The up_link_addr of this SmsAppAddReq.
        :rtype: str
        """
        return self._up_link_addr

    @up_link_addr.setter
    def up_link_addr(self, up_link_addr):
        r"""Sets the up_link_addr of this SmsAppAddReq.

        上行回调地址。只有地域为国内时，

        :param up_link_addr: The up_link_addr of this SmsAppAddReq.
        :type up_link_addr: str
        """
        self._up_link_addr = up_link_addr

    @property
    def show_secret(self):
        r"""Gets the show_secret of this SmsAppAddReq.

        是否在返回体中显示app_secret字段

        :return: The show_secret of this SmsAppAddReq.
        :rtype: bool
        """
        return self._show_secret

    @show_secret.setter
    def show_secret(self, show_secret):
        r"""Sets the show_secret of this SmsAppAddReq.

        是否在返回体中显示app_secret字段

        :param show_secret: The show_secret of this SmsAppAddReq.
        :type show_secret: bool
        """
        self._show_secret = show_secret

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
        if not isinstance(other, SmsAppAddReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
