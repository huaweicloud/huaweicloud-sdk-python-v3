# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component': 'str',
        'verb': 'str',
        'object': 'str',
        'data': 'object'
    }

    attribute_map = {
        'component': 'component',
        'verb': 'verb',
        'object': 'object',
        'data': 'data'
    }

    def __init__(self, component=None, verb=None, object=None, data=None):
        """EventSchema

        The model defined in huaweicloud sdk

        :param component: the component of the codearts snap
        :type component: str
        :param verb: the verb of the action
        :type verb: str
        :param object: the the object of the verb
        :type object: str
        :param data: the data of the event
        :type data: object
        """
        
        

        self._component = None
        self._verb = None
        self._object = None
        self._data = None
        self.discriminator = None

        self.component = component
        if verb is not None:
            self.verb = verb
        if object is not None:
            self.object = object
        if data is not None:
            self.data = data

    @property
    def component(self):
        """Gets the component of this EventSchema.

        the component of the codearts snap

        :return: The component of this EventSchema.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this EventSchema.

        the component of the codearts snap

        :param component: The component of this EventSchema.
        :type component: str
        """
        self._component = component

    @property
    def verb(self):
        """Gets the verb of this EventSchema.

        the verb of the action

        :return: The verb of this EventSchema.
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this EventSchema.

        the verb of the action

        :param verb: The verb of this EventSchema.
        :type verb: str
        """
        self._verb = verb

    @property
    def object(self):
        """Gets the object of this EventSchema.

        the the object of the verb

        :return: The object of this EventSchema.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this EventSchema.

        the the object of the verb

        :param object: The object of this EventSchema.
        :type object: str
        """
        self._object = object

    @property
    def data(self):
        """Gets the data of this EventSchema.

        the data of the event

        :return: The data of this EventSchema.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EventSchema.

        the data of the event

        :param data: The data of this EventSchema.
        :type data: object
        """
        self._data = data

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
        if not isinstance(other, EventSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
