# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAppInstanceHistoryResponseDTO:

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
        'app_version': 'str',
        'version': 'str',
        'values': 'object',
        'update_time': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_version': 'app_version',
        'version': 'version',
        'values': 'values',
        'update_time': 'update_time'
    }

    def __init__(self, app_id=None, app_version=None, version=None, values=None, update_time=None):
        r"""QueryAppInstanceHistoryResponseDTO

        The model defined in huaweicloud sdk

        :param app_id: 应用ID
        :type app_id: str
        :param app_version: 应用版本号
        :type app_version: str
        :param version: 应用实例历史版本号
        :type version: str
        :param values: 应用实例chart配置
        :type values: object
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._app_id = None
        self._app_version = None
        self._version = None
        self._values = None
        self._update_time = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_version is not None:
            self.app_version = app_version
        if version is not None:
            self.version = version
        if values is not None:
            self.values = values
        if update_time is not None:
            self.update_time = update_time

    @property
    def app_id(self):
        r"""Gets the app_id of this QueryAppInstanceHistoryResponseDTO.

        应用ID

        :return: The app_id of this QueryAppInstanceHistoryResponseDTO.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this QueryAppInstanceHistoryResponseDTO.

        应用ID

        :param app_id: The app_id of this QueryAppInstanceHistoryResponseDTO.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_version(self):
        r"""Gets the app_version of this QueryAppInstanceHistoryResponseDTO.

        应用版本号

        :return: The app_version of this QueryAppInstanceHistoryResponseDTO.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this QueryAppInstanceHistoryResponseDTO.

        应用版本号

        :param app_version: The app_version of this QueryAppInstanceHistoryResponseDTO.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def version(self):
        r"""Gets the version of this QueryAppInstanceHistoryResponseDTO.

        应用实例历史版本号

        :return: The version of this QueryAppInstanceHistoryResponseDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this QueryAppInstanceHistoryResponseDTO.

        应用实例历史版本号

        :param version: The version of this QueryAppInstanceHistoryResponseDTO.
        :type version: str
        """
        self._version = version

    @property
    def values(self):
        r"""Gets the values of this QueryAppInstanceHistoryResponseDTO.

        应用实例chart配置

        :return: The values of this QueryAppInstanceHistoryResponseDTO.
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this QueryAppInstanceHistoryResponseDTO.

        应用实例chart配置

        :param values: The values of this QueryAppInstanceHistoryResponseDTO.
        :type values: object
        """
        self._values = values

    @property
    def update_time(self):
        r"""Gets the update_time of this QueryAppInstanceHistoryResponseDTO.

        更新时间

        :return: The update_time of this QueryAppInstanceHistoryResponseDTO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this QueryAppInstanceHistoryResponseDTO.

        更新时间

        :param update_time: The update_time of this QueryAppInstanceHistoryResponseDTO.
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
        if not isinstance(other, QueryAppInstanceHistoryResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
