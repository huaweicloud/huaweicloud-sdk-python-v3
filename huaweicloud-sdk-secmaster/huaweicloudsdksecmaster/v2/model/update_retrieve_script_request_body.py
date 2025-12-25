# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRetrieveScriptRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_name': 'str',
        'directory': 'str',
        'description': 'str',
        'script': 'str'
    }

    attribute_map = {
        'script_name': 'script_name',
        'directory': 'directory',
        'description': 'description',
        'script': 'script'
    }

    def __init__(self, script_name=None, directory=None, description=None, script=None):
        r"""UpdateRetrieveScriptRequestBody

        The model defined in huaweicloud sdk

        :param script_name: 脚本名称
        :type script_name: str
        :param directory: 脚本目录分组名称，长度在1到256个字符之间。
        :type directory: str
        :param description: 脚本的相关描述信息，长度在1到1024个字符之间。
        :type description: str
        :param script: 脚本内容，长度在1到10240个字符之间。
        :type script: str
        """
        
        

        self._script_name = None
        self._directory = None
        self._description = None
        self._script = None
        self.discriminator = None

        if script_name is not None:
            self.script_name = script_name
        if directory is not None:
            self.directory = directory
        if description is not None:
            self.description = description
        if script is not None:
            self.script = script

    @property
    def script_name(self):
        r"""Gets the script_name of this UpdateRetrieveScriptRequestBody.

        脚本名称

        :return: The script_name of this UpdateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this UpdateRetrieveScriptRequestBody.

        脚本名称

        :param script_name: The script_name of this UpdateRetrieveScriptRequestBody.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def directory(self):
        r"""Gets the directory of this UpdateRetrieveScriptRequestBody.

        脚本目录分组名称，长度在1到256个字符之间。

        :return: The directory of this UpdateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this UpdateRetrieveScriptRequestBody.

        脚本目录分组名称，长度在1到256个字符之间。

        :param directory: The directory of this UpdateRetrieveScriptRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def description(self):
        r"""Gets the description of this UpdateRetrieveScriptRequestBody.

        脚本的相关描述信息，长度在1到1024个字符之间。

        :return: The description of this UpdateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateRetrieveScriptRequestBody.

        脚本的相关描述信息，长度在1到1024个字符之间。

        :param description: The description of this UpdateRetrieveScriptRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def script(self):
        r"""Gets the script of this UpdateRetrieveScriptRequestBody.

        脚本内容，长度在1到10240个字符之间。

        :return: The script of this UpdateRetrieveScriptRequestBody.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this UpdateRetrieveScriptRequestBody.

        脚本内容，长度在1到10240个字符之间。

        :param script: The script of this UpdateRetrieveScriptRequestBody.
        :type script: str
        """
        self._script = script

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
        if not isinstance(other, UpdateRetrieveScriptRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
