# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimAlgorithmImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm': 'int',
        'algorithm_id': 'int',
        'limit': 'int',
        'offset': 'int',
        'ordering': 'str',
        'search': 'str',
        'status': 'int',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'algorithm_id': 'algorithm_id',
        'limit': 'limit',
        'offset': 'offset',
        'ordering': 'ordering',
        'search': 'search',
        'status': 'status',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, algorithm=None, algorithm_id=None, limit=None, offset=None, ordering=None, search=None, status=None, type=None, version=None):
        r"""ListSimAlgorithmImagesRequest

        The model defined in huaweicloud sdk

        :param algorithm: 
        :type algorithm: int
        :param algorithm_id: 算法
        :type algorithm_id: int
        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param search: A search term.
        :type search: str
        :param status: 镜像状态  * &#x60;0&#x60; - Success * &#x60;1&#x60; - Pending * &#x60;2&#x60; - Type Error * &#x60;3&#x60; - Not Found * &#x60;4&#x60; - Download Fail * &#x60;5&#x60; - Build Fail * &#x60;32&#x60; - Unknown * &#x60;100&#x60; - Init * &#x60;101&#x60; - Init Failed * &#x60;200&#x60; - To Push * &#x60;201&#x60; - Uploading
        :type status: int
        :param type: 镜像类型  * &#x60;build&#x60; - Build * &#x60;upload&#x60; - Upload
        :type type: str
        :param version: 
        :type version: str
        """
        
        

        self._algorithm = None
        self._algorithm_id = None
        self._limit = None
        self._offset = None
        self._ordering = None
        self._search = None
        self._status = None
        self._type = None
        self._version = None
        self.discriminator = None

        if algorithm is not None:
            self.algorithm = algorithm
        if algorithm_id is not None:
            self.algorithm_id = algorithm_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if ordering is not None:
            self.ordering = ordering
        if search is not None:
            self.search = search
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def algorithm(self):
        r"""Gets the algorithm of this ListSimAlgorithmImagesRequest.

        :return: The algorithm of this ListSimAlgorithmImagesRequest.
        :rtype: int
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this ListSimAlgorithmImagesRequest.

        :param algorithm: The algorithm of this ListSimAlgorithmImagesRequest.
        :type algorithm: int
        """
        self._algorithm = algorithm

    @property
    def algorithm_id(self):
        r"""Gets the algorithm_id of this ListSimAlgorithmImagesRequest.

        算法

        :return: The algorithm_id of this ListSimAlgorithmImagesRequest.
        :rtype: int
        """
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, algorithm_id):
        r"""Sets the algorithm_id of this ListSimAlgorithmImagesRequest.

        算法

        :param algorithm_id: The algorithm_id of this ListSimAlgorithmImagesRequest.
        :type algorithm_id: int
        """
        self._algorithm_id = algorithm_id

    @property
    def limit(self):
        r"""Gets the limit of this ListSimAlgorithmImagesRequest.

        Number of results to return per page.

        :return: The limit of this ListSimAlgorithmImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimAlgorithmImagesRequest.

        Number of results to return per page.

        :param limit: The limit of this ListSimAlgorithmImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSimAlgorithmImagesRequest.

        The initial index from which to return the results.

        :return: The offset of this ListSimAlgorithmImagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimAlgorithmImagesRequest.

        The initial index from which to return the results.

        :param offset: The offset of this ListSimAlgorithmImagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def ordering(self):
        r"""Gets the ordering of this ListSimAlgorithmImagesRequest.

        Which field to use when ordering the results.

        :return: The ordering of this ListSimAlgorithmImagesRequest.
        :rtype: str
        """
        return self._ordering

    @ordering.setter
    def ordering(self, ordering):
        r"""Sets the ordering of this ListSimAlgorithmImagesRequest.

        Which field to use when ordering the results.

        :param ordering: The ordering of this ListSimAlgorithmImagesRequest.
        :type ordering: str
        """
        self._ordering = ordering

    @property
    def search(self):
        r"""Gets the search of this ListSimAlgorithmImagesRequest.

        A search term.

        :return: The search of this ListSimAlgorithmImagesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListSimAlgorithmImagesRequest.

        A search term.

        :param search: The search of this ListSimAlgorithmImagesRequest.
        :type search: str
        """
        self._search = search

    @property
    def status(self):
        r"""Gets the status of this ListSimAlgorithmImagesRequest.

        镜像状态  * `0` - Success * `1` - Pending * `2` - Type Error * `3` - Not Found * `4` - Download Fail * `5` - Build Fail * `32` - Unknown * `100` - Init * `101` - Init Failed * `200` - To Push * `201` - Uploading

        :return: The status of this ListSimAlgorithmImagesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSimAlgorithmImagesRequest.

        镜像状态  * `0` - Success * `1` - Pending * `2` - Type Error * `3` - Not Found * `4` - Download Fail * `5` - Build Fail * `32` - Unknown * `100` - Init * `101` - Init Failed * `200` - To Push * `201` - Uploading

        :param status: The status of this ListSimAlgorithmImagesRequest.
        :type status: int
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListSimAlgorithmImagesRequest.

        镜像类型  * `build` - Build * `upload` - Upload

        :return: The type of this ListSimAlgorithmImagesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListSimAlgorithmImagesRequest.

        镜像类型  * `build` - Build * `upload` - Upload

        :param type: The type of this ListSimAlgorithmImagesRequest.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this ListSimAlgorithmImagesRequest.

        :return: The version of this ListSimAlgorithmImagesRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListSimAlgorithmImagesRequest.

        :param version: The version of this ListSimAlgorithmImagesRequest.
        :type version: str
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
        if not isinstance(other, ListSimAlgorithmImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
