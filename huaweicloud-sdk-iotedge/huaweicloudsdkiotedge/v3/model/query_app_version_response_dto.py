# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAppVersionResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'version': 'str',
        'values': 'object',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'version': 'version',
        'values': 'values',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, app_id=None, version=None, values=None, create_time=None, update_time=None):
        """QueryAppVersionResponseDTO

        The model defined in huaweicloud sdk

        :param app_id: 应用模板ID
        :type app_id: str
        :param version: 应用版本
        :type version: str
        :param values: 应用版本配置
        :type values: object
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        """
        
        

        self._app_id = None
        self._version = None
        self._values = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if version is not None:
            self.version = version
        if values is not None:
            self.values = values
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def app_id(self):
        """Gets the app_id of this QueryAppVersionResponseDTO.

        应用模板ID

        :return: The app_id of this QueryAppVersionResponseDTO.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this QueryAppVersionResponseDTO.

        应用模板ID

        :param app_id: The app_id of this QueryAppVersionResponseDTO.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def version(self):
        """Gets the version of this QueryAppVersionResponseDTO.

        应用版本

        :return: The version of this QueryAppVersionResponseDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this QueryAppVersionResponseDTO.

        应用版本

        :param version: The version of this QueryAppVersionResponseDTO.
        :type version: str
        """
        self._version = version

    @property
    def values(self):
        """Gets the values of this QueryAppVersionResponseDTO.

        应用版本配置

        :return: The values of this QueryAppVersionResponseDTO.
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this QueryAppVersionResponseDTO.

        应用版本配置

        :param values: The values of this QueryAppVersionResponseDTO.
        :type values: object
        """
        self._values = values

    @property
    def create_time(self):
        """Gets the create_time of this QueryAppVersionResponseDTO.

        创建时间

        :return: The create_time of this QueryAppVersionResponseDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryAppVersionResponseDTO.

        创建时间

        :param create_time: The create_time of this QueryAppVersionResponseDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this QueryAppVersionResponseDTO.

        最后一次修改时间

        :return: The update_time of this QueryAppVersionResponseDTO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this QueryAppVersionResponseDTO.

        最后一次修改时间

        :param update_time: The update_time of this QueryAppVersionResponseDTO.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, QueryAppVersionResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
