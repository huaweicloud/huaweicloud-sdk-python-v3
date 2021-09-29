# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Contents:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'content_id': 'int',
        'content': 'list[Content]',
        'index': 'int',
        'selected_temp_name': 'str',
        'data': 'str',
        'data_type': 'int'
    }

    attribute_map = {
        'content_id': 'content_id',
        'content': 'content',
        'index': 'index',
        'selected_temp_name': 'selected_temp_name',
        'data': 'data',
        'data_type': 'data_type'
    }

    def __init__(self, content_id=None, content=None, index=None, selected_temp_name=None, data=None, data_type=None):
        """Contents - a model defined in huaweicloud sdk"""
        
        

        self._content_id = None
        self._content = None
        self._index = None
        self._selected_temp_name = None
        self._data = None
        self._data_type = None
        self.discriminator = None

        if content_id is not None:
            self.content_id = content_id
        if content is not None:
            self.content = content
        if index is not None:
            self.index = index
        if selected_temp_name is not None:
            self.selected_temp_name = selected_temp_name
        if data is not None:
            self.data = data
        if data_type is not None:
            self.data_type = data_type

    @property
    def content_id(self):
        """Gets the content_id of this Contents.

        content_id

        :return: The content_id of this Contents.
        :rtype: int
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this Contents.

        content_id

        :param content_id: The content_id of this Contents.
        :type: int
        """
        self._content_id = content_id

    @property
    def content(self):
        """Gets the content of this Contents.

        content

        :return: The content of this Contents.
        :rtype: list[Content]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Contents.

        content

        :param content: The content of this Contents.
        :type: list[Content]
        """
        self._content = content

    @property
    def index(self):
        """Gets the index of this Contents.

        index

        :return: The index of this Contents.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Contents.

        index

        :param index: The index of this Contents.
        :type: int
        """
        self._index = index

    @property
    def selected_temp_name(self):
        """Gets the selected_temp_name of this Contents.

        selected_temp_name

        :return: The selected_temp_name of this Contents.
        :rtype: str
        """
        return self._selected_temp_name

    @selected_temp_name.setter
    def selected_temp_name(self, selected_temp_name):
        """Sets the selected_temp_name of this Contents.

        selected_temp_name

        :param selected_temp_name: The selected_temp_name of this Contents.
        :type: str
        """
        self._selected_temp_name = selected_temp_name

    @property
    def data(self):
        """Gets the data of this Contents.

        data

        :return: The data of this Contents.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Contents.

        data

        :param data: The data of this Contents.
        :type: str
        """
        self._data = data

    @property
    def data_type(self):
        """Gets the data_type of this Contents.

        data_type

        :return: The data_type of this Contents.
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Contents.

        data_type

        :param data_type: The data_type of this Contents.
        :type: int
        """
        self._data_type = data_type

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
        if not isinstance(other, Contents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
