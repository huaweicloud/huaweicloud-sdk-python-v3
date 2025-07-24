# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoExportPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'events': 'list[str]',
        'prefix': 'str',
        'suffix': 'str'
    }

    attribute_map = {
        'events': 'events',
        'prefix': 'prefix',
        'suffix': 'suffix'
    }

    def __init__(self, events=None, prefix=None, suffix=None):
        r"""AutoExportPolicy

        The model defined in huaweicloud sdk

        :param events: 后端存储自动导出到OBS桶的数据更新类型。 - NEW：表示新增数据，SFS Turbo联动目录下创建的文件，及之后对这些文件进行的元数据和数据修改，会被自动同步到OBS桶里。 - CHANGED：表示修改数据，从OBS桶里导入到SFS Turbo联动目录下的文件，在SFS Turbo上对这些文件所进行的数据和元数据的修改，会被自动同步到OBS桶里。 - DELETED：表示删除数据，在SFS Turbo联动目录下删除文件，OBS桶对应的对象也会被删除，只有被SFS Turbo写入的OBS对象才会被删除。 
        :type events: list[str]
        :param prefix: 后端存储内对象匹配前缀
        :type prefix: str
        :param suffix: 后端存储内对象匹配后缀
        :type suffix: str
        """
        
        

        self._events = None
        self._prefix = None
        self._suffix = None
        self.discriminator = None

        if events is not None:
            self.events = events
        if prefix is not None:
            self.prefix = prefix
        if suffix is not None:
            self.suffix = suffix

    @property
    def events(self):
        r"""Gets the events of this AutoExportPolicy.

        后端存储自动导出到OBS桶的数据更新类型。 - NEW：表示新增数据，SFS Turbo联动目录下创建的文件，及之后对这些文件进行的元数据和数据修改，会被自动同步到OBS桶里。 - CHANGED：表示修改数据，从OBS桶里导入到SFS Turbo联动目录下的文件，在SFS Turbo上对这些文件所进行的数据和元数据的修改，会被自动同步到OBS桶里。 - DELETED：表示删除数据，在SFS Turbo联动目录下删除文件，OBS桶对应的对象也会被删除，只有被SFS Turbo写入的OBS对象才会被删除。 

        :return: The events of this AutoExportPolicy.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this AutoExportPolicy.

        后端存储自动导出到OBS桶的数据更新类型。 - NEW：表示新增数据，SFS Turbo联动目录下创建的文件，及之后对这些文件进行的元数据和数据修改，会被自动同步到OBS桶里。 - CHANGED：表示修改数据，从OBS桶里导入到SFS Turbo联动目录下的文件，在SFS Turbo上对这些文件所进行的数据和元数据的修改，会被自动同步到OBS桶里。 - DELETED：表示删除数据，在SFS Turbo联动目录下删除文件，OBS桶对应的对象也会被删除，只有被SFS Turbo写入的OBS对象才会被删除。 

        :param events: The events of this AutoExportPolicy.
        :type events: list[str]
        """
        self._events = events

    @property
    def prefix(self):
        r"""Gets the prefix of this AutoExportPolicy.

        后端存储内对象匹配前缀

        :return: The prefix of this AutoExportPolicy.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this AutoExportPolicy.

        后端存储内对象匹配前缀

        :param prefix: The prefix of this AutoExportPolicy.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def suffix(self):
        r"""Gets the suffix of this AutoExportPolicy.

        后端存储内对象匹配后缀

        :return: The suffix of this AutoExportPolicy.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        r"""Sets the suffix of this AutoExportPolicy.

        后端存储内对象匹配后缀

        :param suffix: The suffix of this AutoExportPolicy.
        :type suffix: str
        """
        self._suffix = suffix

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
        if not isinstance(other, AutoExportPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
