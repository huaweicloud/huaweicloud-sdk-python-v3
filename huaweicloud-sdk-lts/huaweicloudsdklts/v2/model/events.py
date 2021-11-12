# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Events:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'annotations': 'Annotations',
        'metadata': 'Metadata',
        'arrives_at': 'object',
        'ends_at': 'object',
        'id': 'str',
        'starts_at': 'object',
        'timeout': 'object',
        'type': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'metadata': 'metadata',
        'arrives_at': 'arrives_at',
        'ends_at': 'ends_at',
        'id': 'id',
        'starts_at': 'starts_at',
        'timeout': 'timeout',
        'type': 'type'
    }

    def __init__(self, annotations=None, metadata=None, arrives_at=None, ends_at=None, id=None, starts_at=None, timeout=None, type=None):
        """Events - a model defined in huaweicloud sdk"""
        
        

        self._annotations = None
        self._metadata = None
        self._arrives_at = None
        self._ends_at = None
        self._id = None
        self._starts_at = None
        self._timeout = None
        self._type = None
        self.discriminator = None

        self.annotations = annotations
        self.metadata = metadata
        self.arrives_at = arrives_at
        self.ends_at = ends_at
        self.id = id
        self.starts_at = starts_at
        self.timeout = timeout
        self.type = type

    @property
    def annotations(self):
        """Gets the annotations of this Events.

        告警详情

        :return: The annotations of this Events.
        :rtype: Annotations
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Events.

        告警详情

        :param annotations: The annotations of this Events.
        :type: Annotations
        """
        self._annotations = annotations

    @property
    def metadata(self):
        """Gets the metadata of this Events.

        告警信息

        :return: The metadata of this Events.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Events.

        告警信息

        :param metadata: The metadata of this Events.
        :type: Metadata
        """
        self._metadata = metadata

    @property
    def arrives_at(self):
        """Gets the arrives_at of this Events.

        到达时间(时间戳)

        :return: The arrives_at of this Events.
        :rtype: object
        """
        return self._arrives_at

    @arrives_at.setter
    def arrives_at(self, arrives_at):
        """Sets the arrives_at of this Events.

        到达时间(时间戳)

        :param arrives_at: The arrives_at of this Events.
        :type: object
        """
        self._arrives_at = arrives_at

    @property
    def ends_at(self):
        """Gets the ends_at of this Events.

        告警清除时间(时间戳)

        :return: The ends_at of this Events.
        :rtype: object
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this Events.

        告警清除时间(时间戳)

        :param ends_at: The ends_at of this Events.
        :type: object
        """
        self._ends_at = ends_at

    @property
    def id(self):
        """Gets the id of this Events.

        告警id

        :return: The id of this Events.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Events.

        告警id

        :param id: The id of this Events.
        :type: str
        """
        self._id = id

    @property
    def starts_at(self):
        """Gets the starts_at of this Events.

        告警产生时间(时间戳)

        :return: The starts_at of this Events.
        :rtype: object
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this Events.

        告警产生时间(时间戳)

        :param starts_at: The starts_at of this Events.
        :type: object
        """
        self._starts_at = starts_at

    @property
    def timeout(self):
        """Gets the timeout of this Events.

        告警自动清除时间(时间戳)

        :return: The timeout of this Events.
        :rtype: object
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Events.

        告警自动清除时间(时间戳)

        :param timeout: The timeout of this Events.
        :type: object
        """
        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this Events.

        告警规则类型(SQL/关键词)

        :return: The type of this Events.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Events.

        告警规则类型(SQL/关键词)

        :param type: The type of this Events.
        :type: str
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
        if not isinstance(other, Events):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
