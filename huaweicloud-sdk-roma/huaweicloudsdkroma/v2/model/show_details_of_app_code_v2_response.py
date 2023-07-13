# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailsOfAppCodeV2Response(SdkResponse):

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
        'create_time': 'datetime'
    }

    attribute_map = {
        'app_code': 'app_code',
        'id': 'id',
        'app_id': 'app_id',
        'create_time': 'create_time'
    }

    def __init__(self, app_code=None, id=None, app_id=None, create_time=None):
        """ShowDetailsOfAppCodeV2Response

        The model defined in huaweicloud sdk

        :param app_code: App Code值  支持英文，+_!@#$%+/&#x3D;，且只能以英文和+、/开头。
        :type app_code: str
        :param id: 编号
        :type id: str
        :param app_id: 应用编号
        :type app_id: str
        :param create_time: 创建时间
        :type create_time: datetime
        """
        
        super(ShowDetailsOfAppCodeV2Response, self).__init__()

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
        """Gets the app_code of this ShowDetailsOfAppCodeV2Response.

        App Code值  支持英文，+_!@#$%+/=，且只能以英文和+、/开头。

        :return: The app_code of this ShowDetailsOfAppCodeV2Response.
        :rtype: str
        """
        return self._app_code

    @app_code.setter
    def app_code(self, app_code):
        """Sets the app_code of this ShowDetailsOfAppCodeV2Response.

        App Code值  支持英文，+_!@#$%+/=，且只能以英文和+、/开头。

        :param app_code: The app_code of this ShowDetailsOfAppCodeV2Response.
        :type app_code: str
        """
        self._app_code = app_code

    @property
    def id(self):
        """Gets the id of this ShowDetailsOfAppCodeV2Response.

        编号

        :return: The id of this ShowDetailsOfAppCodeV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDetailsOfAppCodeV2Response.

        编号

        :param id: The id of this ShowDetailsOfAppCodeV2Response.
        :type id: str
        """
        self._id = id

    @property
    def app_id(self):
        """Gets the app_id of this ShowDetailsOfAppCodeV2Response.

        应用编号

        :return: The app_id of this ShowDetailsOfAppCodeV2Response.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowDetailsOfAppCodeV2Response.

        应用编号

        :param app_id: The app_id of this ShowDetailsOfAppCodeV2Response.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowDetailsOfAppCodeV2Response.

        创建时间

        :return: The create_time of this ShowDetailsOfAppCodeV2Response.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowDetailsOfAppCodeV2Response.

        创建时间

        :param create_time: The create_time of this ShowDetailsOfAppCodeV2Response.
        :type create_time: datetime
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
        if not isinstance(other, ShowDetailsOfAppCodeV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
