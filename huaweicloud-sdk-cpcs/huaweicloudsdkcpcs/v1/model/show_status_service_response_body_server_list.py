# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatusServiceResponseBodyServerList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_type': 'str',
        'app_list': 'list[ShowStatusAppItem]'
    }

    attribute_map = {
        'server_type': 'server_type',
        'app_list': 'app_list'
    }

    def __init__(self, server_type=None, app_list=None):
        r"""ShowStatusServiceResponseBodyServerList

        The model defined in huaweicloud sdk

        :param server_type: 服务类型
        :type server_type: str
        :param app_list: 应用列表
        :type app_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusAppItem`]
        """
        
        

        self._server_type = None
        self._app_list = None
        self.discriminator = None

        if server_type is not None:
            self.server_type = server_type
        if app_list is not None:
            self.app_list = app_list

    @property
    def server_type(self):
        r"""Gets the server_type of this ShowStatusServiceResponseBodyServerList.

        服务类型

        :return: The server_type of this ShowStatusServiceResponseBodyServerList.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ShowStatusServiceResponseBodyServerList.

        服务类型

        :param server_type: The server_type of this ShowStatusServiceResponseBodyServerList.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def app_list(self):
        r"""Gets the app_list of this ShowStatusServiceResponseBodyServerList.

        应用列表

        :return: The app_list of this ShowStatusServiceResponseBodyServerList.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusAppItem`]
        """
        return self._app_list

    @app_list.setter
    def app_list(self, app_list):
        r"""Sets the app_list of this ShowStatusServiceResponseBodyServerList.

        应用列表

        :param app_list: The app_list of this ShowStatusServiceResponseBodyServerList.
        :type app_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusAppItem`]
        """
        self._app_list = app_list

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
        if not isinstance(other, ShowStatusServiceResponseBodyServerList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
