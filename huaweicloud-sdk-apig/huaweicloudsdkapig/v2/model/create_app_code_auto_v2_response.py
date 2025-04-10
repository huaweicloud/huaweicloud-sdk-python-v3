# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppCodeAutoV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_code': 'str',
        'id': 'str',
        'app_id': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'app_code': 'app_code',
        'id': 'id',
        'app_id': 'app_id',
        'create_time': 'create_time'
    }

    def __init__(self, app_code=None, id=None, app_id=None, create_time=None):
        r"""CreateAppCodeAutoV2Response

        The model defined in huaweicloud sdk

        :param app_code: App Code值  支持英文、数字，+_!@#$%-/&#x3D;，且只能以英文、数字和+、/开头，64-180个字符。
        :type app_code: str
        :param id: 编号
        :type id: str
        :param app_id: 应用编号
        :type app_id: str
        :param create_time: 创建时间
        :type create_time: str
        """
        
        super(CreateAppCodeAutoV2Response, self).__init__()

        self._app_code = None
        self._id = None
        self._app_id = None
        self._create_time = None
        self.discriminator = None

        self.app_code = app_code
        if id is not None:
            self.id = id
        if app_id is not None:
            self.app_id = app_id
        if create_time is not None:
            self.create_time = create_time

    @property
    def app_code(self):
        r"""Gets the app_code of this CreateAppCodeAutoV2Response.

        App Code值  支持英文、数字，+_!@#$%-/=，且只能以英文、数字和+、/开头，64-180个字符。

        :return: The app_code of this CreateAppCodeAutoV2Response.
        :rtype: str
        """
        return self._app_code

    @app_code.setter
    def app_code(self, app_code):
        r"""Sets the app_code of this CreateAppCodeAutoV2Response.

        App Code值  支持英文、数字，+_!@#$%-/=，且只能以英文、数字和+、/开头，64-180个字符。

        :param app_code: The app_code of this CreateAppCodeAutoV2Response.
        :type app_code: str
        """
        self._app_code = app_code

    @property
    def id(self):
        r"""Gets the id of this CreateAppCodeAutoV2Response.

        编号

        :return: The id of this CreateAppCodeAutoV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateAppCodeAutoV2Response.

        编号

        :param id: The id of this CreateAppCodeAutoV2Response.
        :type id: str
        """
        self._id = id

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateAppCodeAutoV2Response.

        应用编号

        :return: The app_id of this CreateAppCodeAutoV2Response.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateAppCodeAutoV2Response.

        应用编号

        :param app_id: The app_id of this CreateAppCodeAutoV2Response.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateAppCodeAutoV2Response.

        创建时间

        :return: The create_time of this CreateAppCodeAutoV2Response.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateAppCodeAutoV2Response.

        创建时间

        :param create_time: The create_time of this CreateAppCodeAutoV2Response.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, CreateAppCodeAutoV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
