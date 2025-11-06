# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageNonCompliantAppInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'app_name': 'str',
        'app_path': 'str',
        'app_version': 'str',
        'layer_digest': 'str'
    }

    attribute_map = {
        'id': 'id',
        'app_name': 'app_name',
        'app_path': 'app_path',
        'app_version': 'app_version',
        'layer_digest': 'layer_digest'
    }

    def __init__(self, id=None, app_name=None, app_path=None, app_version=None, layer_digest=None):
        r"""ImageNonCompliantAppInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: id **取值范围**: 字符长度0-128位 
        :type id: str
        :param app_name: **参数解释**: 不合规软件名称 **取值范围**: 字符长度0-128位 
        :type app_name: str
        :param app_path: **参数解释**: 不合规软件路径 **取值范围**: 字符长度0-128位 
        :type app_path: str
        :param app_version: **参数解释**: 不合规软件版本 **取值范围**: 字符长度0-64位 
        :type app_version: str
        :param layer_digest: **参数解释**: 层digest **取值范围**: 字符长度0-128位 
        :type layer_digest: str
        """
        
        

        self._id = None
        self._app_name = None
        self._app_path = None
        self._app_version = None
        self._layer_digest = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if app_name is not None:
            self.app_name = app_name
        if app_path is not None:
            self.app_path = app_path
        if app_version is not None:
            self.app_version = app_version
        if layer_digest is not None:
            self.layer_digest = layer_digest

    @property
    def id(self):
        r"""Gets the id of this ImageNonCompliantAppInfo.

        **参数解释**: id **取值范围**: 字符长度0-128位 

        :return: The id of this ImageNonCompliantAppInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageNonCompliantAppInfo.

        **参数解释**: id **取值范围**: 字符长度0-128位 

        :param id: The id of this ImageNonCompliantAppInfo.
        :type id: str
        """
        self._id = id

    @property
    def app_name(self):
        r"""Gets the app_name of this ImageNonCompliantAppInfo.

        **参数解释**: 不合规软件名称 **取值范围**: 字符长度0-128位 

        :return: The app_name of this ImageNonCompliantAppInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ImageNonCompliantAppInfo.

        **参数解释**: 不合规软件名称 **取值范围**: 字符长度0-128位 

        :param app_name: The app_name of this ImageNonCompliantAppInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_path(self):
        r"""Gets the app_path of this ImageNonCompliantAppInfo.

        **参数解释**: 不合规软件路径 **取值范围**: 字符长度0-128位 

        :return: The app_path of this ImageNonCompliantAppInfo.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this ImageNonCompliantAppInfo.

        **参数解释**: 不合规软件路径 **取值范围**: 字符长度0-128位 

        :param app_path: The app_path of this ImageNonCompliantAppInfo.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def app_version(self):
        r"""Gets the app_version of this ImageNonCompliantAppInfo.

        **参数解释**: 不合规软件版本 **取值范围**: 字符长度0-64位 

        :return: The app_version of this ImageNonCompliantAppInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this ImageNonCompliantAppInfo.

        **参数解释**: 不合规软件版本 **取值范围**: 字符长度0-64位 

        :param app_version: The app_version of this ImageNonCompliantAppInfo.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def layer_digest(self):
        r"""Gets the layer_digest of this ImageNonCompliantAppInfo.

        **参数解释**: 层digest **取值范围**: 字符长度0-128位 

        :return: The layer_digest of this ImageNonCompliantAppInfo.
        :rtype: str
        """
        return self._layer_digest

    @layer_digest.setter
    def layer_digest(self, layer_digest):
        r"""Sets the layer_digest of this ImageNonCompliantAppInfo.

        **参数解释**: 层digest **取值范围**: 字符长度0-128位 

        :param layer_digest: The layer_digest of this ImageNonCompliantAppInfo.
        :type layer_digest: str
        """
        self._layer_digest = layer_digest

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageNonCompliantAppInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
