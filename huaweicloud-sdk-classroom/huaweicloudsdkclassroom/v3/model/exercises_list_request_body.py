# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExercisesListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter': 'ExerciseFilter',
        'page_size': 'int',
        'start_index': 'int'
    }

    attribute_map = {
        'filter': 'filter',
        'page_size': 'page_size',
        'start_index': 'start_index'
    }

    def __init__(self, filter=None, page_size=None, start_index=None):
        """ExercisesListRequestBody

        The model defined in huaweicloud sdk

        :param filter: 
        :type filter: :class:`huaweicloudsdkclassroom.v3.ExerciseFilter`
        :param page_size: 每页数量
        :type page_size: int
        :param start_index: 起始页
        :type start_index: int
        """
        
        

        self._filter = None
        self._page_size = None
        self._start_index = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if page_size is not None:
            self.page_size = page_size
        if start_index is not None:
            self.start_index = start_index

    @property
    def filter(self):
        """Gets the filter of this ExercisesListRequestBody.

        :return: The filter of this ExercisesListRequestBody.
        :rtype: :class:`huaweicloudsdkclassroom.v3.ExerciseFilter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ExercisesListRequestBody.

        :param filter: The filter of this ExercisesListRequestBody.
        :type filter: :class:`huaweicloudsdkclassroom.v3.ExerciseFilter`
        """
        self._filter = filter

    @property
    def page_size(self):
        """Gets the page_size of this ExercisesListRequestBody.

        每页数量

        :return: The page_size of this ExercisesListRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ExercisesListRequestBody.

        每页数量

        :param page_size: The page_size of this ExercisesListRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def start_index(self):
        """Gets the start_index of this ExercisesListRequestBody.

        起始页

        :return: The start_index of this ExercisesListRequestBody.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this ExercisesListRequestBody.

        起始页

        :param start_index: The start_index of this ExercisesListRequestBody.
        :type start_index: int
        """
        self._start_index = start_index

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
        if not isinstance(other, ExercisesListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
