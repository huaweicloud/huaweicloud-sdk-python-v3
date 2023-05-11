# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskOutputLocalpath:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mount_source_path': 'str',
        'data_category': 'list[str]'
    }

    attribute_map = {
        'mount_source_path': 'mount_source_path',
        'data_category': 'data_category'
    }

    def __init__(self, mount_source_path=None, data_category=None):
        """TaskOutputLocalpath

        The model defined in huaweicloud sdk

        :param mount_source_path: 挂载的源路径，存放作业运行结果的路径，选用localpath类型输出时必填。必须为linux路径，且为选用的边缘运行池挂载路径的子路径，长度不超过255。
        :type mount_source_path: str
        :param data_category: 作业输出数据类别的列表，选填，仅部分服务需要。当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据。
        :type data_category: list[str]
        """
        
        

        self._mount_source_path = None
        self._data_category = None
        self.discriminator = None

        self.mount_source_path = mount_source_path
        if data_category is not None:
            self.data_category = data_category

    @property
    def mount_source_path(self):
        """Gets the mount_source_path of this TaskOutputLocalpath.

        挂载的源路径，存放作业运行结果的路径，选用localpath类型输出时必填。必须为linux路径，且为选用的边缘运行池挂载路径的子路径，长度不超过255。

        :return: The mount_source_path of this TaskOutputLocalpath.
        :rtype: str
        """
        return self._mount_source_path

    @mount_source_path.setter
    def mount_source_path(self, mount_source_path):
        """Sets the mount_source_path of this TaskOutputLocalpath.

        挂载的源路径，存放作业运行结果的路径，选用localpath类型输出时必填。必须为linux路径，且为选用的边缘运行池挂载路径的子路径，长度不超过255。

        :param mount_source_path: The mount_source_path of this TaskOutputLocalpath.
        :type mount_source_path: str
        """
        self._mount_source_path = mount_source_path

    @property
    def data_category(self):
        """Gets the data_category of this TaskOutputLocalpath.

        作业输出数据类别的列表，选填，仅部分服务需要。当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据。

        :return: The data_category of this TaskOutputLocalpath.
        :rtype: list[str]
        """
        return self._data_category

    @data_category.setter
    def data_category(self, data_category):
        """Sets the data_category of this TaskOutputLocalpath.

        作业输出数据类别的列表，选填，仅部分服务需要。当输出类型下有这个列表时，表示希望这个输出类型下存放dataCategory列表内的数据。

        :param data_category: The data_category of this TaskOutputLocalpath.
        :type data_category: list[str]
        """
        self._data_category = data_category

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
        if not isinstance(other, TaskOutputLocalpath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
