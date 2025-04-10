# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetadataTask:

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
        'name': 'str',
        'start_date': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'start_date': 'start_date',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, start_date=None, status=None, type=None):
        r"""MetadataTask

        The model defined in huaweicloud sdk

        :param id: 元数据迁移任务ID。
        :type id: str
        :param name: 元数据迁移任务名称。
        :type name: str
        :param start_date: 元数据迁移任务开始时间。
        :type start_date: str
        :param status: 元数据迁移任务状态。
        :type status: str
        :param type: 元数据迁移类型。
        :type type: str
        """
        
        

        self._id = None
        self._name = None
        self._start_date = None
        self._status = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this MetadataTask.

        元数据迁移任务ID。

        :return: The id of this MetadataTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MetadataTask.

        元数据迁移任务ID。

        :param id: The id of this MetadataTask.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this MetadataTask.

        元数据迁移任务名称。

        :return: The name of this MetadataTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MetadataTask.

        元数据迁移任务名称。

        :param name: The name of this MetadataTask.
        :type name: str
        """
        self._name = name

    @property
    def start_date(self):
        r"""Gets the start_date of this MetadataTask.

        元数据迁移任务开始时间。

        :return: The start_date of this MetadataTask.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this MetadataTask.

        元数据迁移任务开始时间。

        :param start_date: The start_date of this MetadataTask.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def status(self):
        r"""Gets the status of this MetadataTask.

        元数据迁移任务状态。

        :return: The status of this MetadataTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MetadataTask.

        元数据迁移任务状态。

        :param status: The status of this MetadataTask.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this MetadataTask.

        元数据迁移类型。

        :return: The type of this MetadataTask.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MetadataTask.

        元数据迁移类型。

        :param type: The type of this MetadataTask.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, MetadataTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
