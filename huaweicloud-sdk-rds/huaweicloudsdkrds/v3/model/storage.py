# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Storage:

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
        'az_status': 'dict(str, str)',
        'support_compute_group_type': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'az_status': 'az_status',
        'support_compute_group_type': 'support_compute_group_type'
    }

    def __init__(self, name=None, az_status=None, support_compute_group_type=None):
        """Storage

        The model defined in huaweicloud sdk

        :param name: 磁盘类型名称，可能取值如下： - ULTRAHIGH：表示SSD。 - LOCALSSD：表示本地SSD。 - CLOUDSSD：表示SSD云盘，仅支持通用型和独享型规格实例。 - ESSD：表示极速型SSD，仅支持独享型规格实例。
        :type name: str
        :param az_status: 其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。
        :type az_status: dict(str, str)
        :param support_compute_group_type: 性能规格，包含以下状态： - normal：通用增强型。 - normal2：通用增强Ⅱ型。 - armFlavors：鲲鹏通用增强型。 - dedicicatenormal ：x86独享型。 - armlocalssd：鲲鹏通用型。 - normallocalssd：x86通用型。 - general：通用型。 - dedicated：独享型，仅云盘SSD支持。 - rapid：独享型，仅极速型SSD支持。 - bigmen：超大内存型。
        :type support_compute_group_type: list[str]
        """
        
        

        self._name = None
        self._az_status = None
        self._support_compute_group_type = None
        self.discriminator = None

        self.name = name
        self.az_status = az_status
        if support_compute_group_type is not None:
            self.support_compute_group_type = support_compute_group_type

    @property
    def name(self):
        """Gets the name of this Storage.

        磁盘类型名称，可能取值如下： - ULTRAHIGH：表示SSD。 - LOCALSSD：表示本地SSD。 - CLOUDSSD：表示SSD云盘，仅支持通用型和独享型规格实例。 - ESSD：表示极速型SSD，仅支持独享型规格实例。

        :return: The name of this Storage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Storage.

        磁盘类型名称，可能取值如下： - ULTRAHIGH：表示SSD。 - LOCALSSD：表示本地SSD。 - CLOUDSSD：表示SSD云盘，仅支持通用型和独享型规格实例。 - ESSD：表示极速型SSD，仅支持独享型规格实例。

        :param name: The name of this Storage.
        :type name: str
        """
        self._name = name

    @property
    def az_status(self):
        """Gets the az_status of this Storage.

        其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。

        :return: The az_status of this Storage.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this Storage.

        其中key是可用区编号，value是规格所在az的状态，包含以下状态： - normal，在售。 - unsupported，暂不支持该规格。 - sellout，售罄。

        :param az_status: The az_status of this Storage.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

    @property
    def support_compute_group_type(self):
        """Gets the support_compute_group_type of this Storage.

        性能规格，包含以下状态： - normal：通用增强型。 - normal2：通用增强Ⅱ型。 - armFlavors：鲲鹏通用增强型。 - dedicicatenormal ：x86独享型。 - armlocalssd：鲲鹏通用型。 - normallocalssd：x86通用型。 - general：通用型。 - dedicated：独享型，仅云盘SSD支持。 - rapid：独享型，仅极速型SSD支持。 - bigmen：超大内存型。

        :return: The support_compute_group_type of this Storage.
        :rtype: list[str]
        """
        return self._support_compute_group_type

    @support_compute_group_type.setter
    def support_compute_group_type(self, support_compute_group_type):
        """Sets the support_compute_group_type of this Storage.

        性能规格，包含以下状态： - normal：通用增强型。 - normal2：通用增强Ⅱ型。 - armFlavors：鲲鹏通用增强型。 - dedicicatenormal ：x86独享型。 - armlocalssd：鲲鹏通用型。 - normallocalssd：x86通用型。 - general：通用型。 - dedicated：独享型，仅云盘SSD支持。 - rapid：独享型，仅极速型SSD支持。 - bigmen：超大内存型。

        :param support_compute_group_type: The support_compute_group_type of this Storage.
        :type support_compute_group_type: list[str]
        """
        self._support_compute_group_type = support_compute_group_type

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
        if not isinstance(other, Storage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
