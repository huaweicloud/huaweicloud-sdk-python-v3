# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateModelInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'current_version_id': 'str',
        'version': 'ModelVersionInput'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'current_version_id': 'current_version_id',
        'version': 'version'
    }

    def __init__(self, name=None, description=None, current_version_id=None, version=None):
        r"""UpdateModelInput

        The model defined in huaweicloud sdk

        :param name: 一个Model的名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param description: 描述信息
        :type description: str
        :param current_version_id: 模型版本ID，32~36位的英文、数字、短横组合，系统自动生成无法修改，输入不生效。
        :type current_version_id: str
        :param version: 
        :type version: :class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInput`
        """
        
        

        self._name = None
        self._description = None
        self._current_version_id = None
        self._version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if current_version_id is not None:
            self.current_version_id = current_version_id
        if version is not None:
            self.version = version

    @property
    def name(self):
        r"""Gets the name of this UpdateModelInput.

        一个Model的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this UpdateModelInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateModelInput.

        一个Model的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this UpdateModelInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateModelInput.

        描述信息

        :return: The description of this UpdateModelInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateModelInput.

        描述信息

        :param description: The description of this UpdateModelInput.
        :type description: str
        """
        self._description = description

    @property
    def current_version_id(self):
        r"""Gets the current_version_id of this UpdateModelInput.

        模型版本ID，32~36位的英文、数字、短横组合，系统自动生成无法修改，输入不生效。

        :return: The current_version_id of this UpdateModelInput.
        :rtype: str
        """
        return self._current_version_id

    @current_version_id.setter
    def current_version_id(self, current_version_id):
        r"""Sets the current_version_id of this UpdateModelInput.

        模型版本ID，32~36位的英文、数字、短横组合，系统自动生成无法修改，输入不生效。

        :param current_version_id: The current_version_id of this UpdateModelInput.
        :type current_version_id: str
        """
        self._current_version_id = current_version_id

    @property
    def version(self):
        r"""Gets the version of this UpdateModelInput.

        :return: The version of this UpdateModelInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInput`
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateModelInput.

        :param version: The version of this UpdateModelInput.
        :type version: :class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInput`
        """
        self._version = version

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
        if not isinstance(other, UpdateModelInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
