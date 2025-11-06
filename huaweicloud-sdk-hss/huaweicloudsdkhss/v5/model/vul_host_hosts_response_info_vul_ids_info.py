# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHostHostsResponseInfoVulIdsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'linux_vul_id_list': 'list[str]',
        'windows_vul_id_list': 'list[str]',
        'webcms_vul_id_list': 'list[str]',
        'app_vul_id_list': 'list[str]',
        'urgent_vul_id_list': 'list[str]'
    }

    attribute_map = {
        'linux_vul_id_list': 'linux_vul_id_list',
        'windows_vul_id_list': 'windows_vul_id_list',
        'webcms_vul_id_list': 'webcms_vul_id_list',
        'app_vul_id_list': 'app_vul_id_list',
        'urgent_vul_id_list': 'urgent_vul_id_list'
    }

    def __init__(self, linux_vul_id_list=None, windows_vul_id_list=None, webcms_vul_id_list=None, app_vul_id_list=None, urgent_vul_id_list=None):
        r"""VulHostHostsResponseInfoVulIdsInfo

        The model defined in huaweicloud sdk

        :param linux_vul_id_list: **参数解释**: Linux漏洞的漏洞id列表 
        :type linux_vul_id_list: list[str]
        :param windows_vul_id_list: **参数解释**: Windows漏洞的漏洞id列表 
        :type windows_vul_id_list: list[str]
        :param webcms_vul_id_list: **参数解释**: Web-CMS漏洞的漏洞id列表 
        :type webcms_vul_id_list: list[str]
        :param app_vul_id_list: **参数解释**: 应用漏洞的漏洞id列表 
        :type app_vul_id_list: list[str]
        :param urgent_vul_id_list: **参数解释**: 应急漏洞的漏洞id列表 
        :type urgent_vul_id_list: list[str]
        """
        
        

        self._linux_vul_id_list = None
        self._windows_vul_id_list = None
        self._webcms_vul_id_list = None
        self._app_vul_id_list = None
        self._urgent_vul_id_list = None
        self.discriminator = None

        if linux_vul_id_list is not None:
            self.linux_vul_id_list = linux_vul_id_list
        if windows_vul_id_list is not None:
            self.windows_vul_id_list = windows_vul_id_list
        if webcms_vul_id_list is not None:
            self.webcms_vul_id_list = webcms_vul_id_list
        if app_vul_id_list is not None:
            self.app_vul_id_list = app_vul_id_list
        if urgent_vul_id_list is not None:
            self.urgent_vul_id_list = urgent_vul_id_list

    @property
    def linux_vul_id_list(self):
        r"""Gets the linux_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: Linux漏洞的漏洞id列表 

        :return: The linux_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :rtype: list[str]
        """
        return self._linux_vul_id_list

    @linux_vul_id_list.setter
    def linux_vul_id_list(self, linux_vul_id_list):
        r"""Sets the linux_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: Linux漏洞的漏洞id列表 

        :param linux_vul_id_list: The linux_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :type linux_vul_id_list: list[str]
        """
        self._linux_vul_id_list = linux_vul_id_list

    @property
    def windows_vul_id_list(self):
        r"""Gets the windows_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: Windows漏洞的漏洞id列表 

        :return: The windows_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :rtype: list[str]
        """
        return self._windows_vul_id_list

    @windows_vul_id_list.setter
    def windows_vul_id_list(self, windows_vul_id_list):
        r"""Sets the windows_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: Windows漏洞的漏洞id列表 

        :param windows_vul_id_list: The windows_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :type windows_vul_id_list: list[str]
        """
        self._windows_vul_id_list = windows_vul_id_list

    @property
    def webcms_vul_id_list(self):
        r"""Gets the webcms_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: Web-CMS漏洞的漏洞id列表 

        :return: The webcms_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :rtype: list[str]
        """
        return self._webcms_vul_id_list

    @webcms_vul_id_list.setter
    def webcms_vul_id_list(self, webcms_vul_id_list):
        r"""Sets the webcms_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: Web-CMS漏洞的漏洞id列表 

        :param webcms_vul_id_list: The webcms_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :type webcms_vul_id_list: list[str]
        """
        self._webcms_vul_id_list = webcms_vul_id_list

    @property
    def app_vul_id_list(self):
        r"""Gets the app_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: 应用漏洞的漏洞id列表 

        :return: The app_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :rtype: list[str]
        """
        return self._app_vul_id_list

    @app_vul_id_list.setter
    def app_vul_id_list(self, app_vul_id_list):
        r"""Sets the app_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: 应用漏洞的漏洞id列表 

        :param app_vul_id_list: The app_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :type app_vul_id_list: list[str]
        """
        self._app_vul_id_list = app_vul_id_list

    @property
    def urgent_vul_id_list(self):
        r"""Gets the urgent_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: 应急漏洞的漏洞id列表 

        :return: The urgent_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :rtype: list[str]
        """
        return self._urgent_vul_id_list

    @urgent_vul_id_list.setter
    def urgent_vul_id_list(self, urgent_vul_id_list):
        r"""Sets the urgent_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.

        **参数解释**: 应急漏洞的漏洞id列表 

        :param urgent_vul_id_list: The urgent_vul_id_list of this VulHostHostsResponseInfoVulIdsInfo.
        :type urgent_vul_id_list: list[str]
        """
        self._urgent_vul_id_list = urgent_vul_id_list

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
        if not isinstance(other, VulHostHostsResponseInfoVulIdsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
