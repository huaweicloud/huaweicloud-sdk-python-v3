# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimBatchesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm_image_version': 'str',
        'algorithm_name': 'str',
        'batch_config_id': 'int',
        'description': 'str',
        'generalization_id': 'int',
        'id': 'int',
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'ordering': 'str',
        'search': 'str',
        'status': 'int'
    }

    attribute_map = {
        'algorithm_image_version': 'algorithm_image_version',
        'algorithm_name': 'algorithm_name',
        'batch_config_id': 'batch_config_id',
        'description': 'description',
        'generalization_id': 'generalization_id',
        'id': 'id',
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'ordering': 'ordering',
        'search': 'search',
        'status': 'status'
    }

    def __init__(self, algorithm_image_version=None, algorithm_name=None, batch_config_id=None, description=None, generalization_id=None, id=None, limit=None, name=None, offset=None, ordering=None, search=None, status=None):
        r"""ListSimBatchesRequest

        The model defined in huaweicloud sdk

        :param algorithm_image_version: 算法镜像版本
        :type algorithm_image_version: str
        :param algorithm_name: 算法名称
        :type algorithm_name: str
        :param batch_config_id: 关联batch配置
        :type batch_config_id: int
        :param description: 描述
        :type description: str
        :param generalization_id: 泛化任务id
        :type generalization_id: int
        :param id: 
        :type id: int
        :param limit: Number of results to return per page.
        :type limit: int
        :param name: 
        :type name: str
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param search: A search term.
        :type search: str
        :param status: 任务状态
        :type status: int
        """
        
        

        self._algorithm_image_version = None
        self._algorithm_name = None
        self._batch_config_id = None
        self._description = None
        self._generalization_id = None
        self._id = None
        self._limit = None
        self._name = None
        self._offset = None
        self._ordering = None
        self._search = None
        self._status = None
        self.discriminator = None

        if algorithm_image_version is not None:
            self.algorithm_image_version = algorithm_image_version
        if algorithm_name is not None:
            self.algorithm_name = algorithm_name
        if batch_config_id is not None:
            self.batch_config_id = batch_config_id
        if description is not None:
            self.description = description
        if generalization_id is not None:
            self.generalization_id = generalization_id
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if ordering is not None:
            self.ordering = ordering
        if search is not None:
            self.search = search
        if status is not None:
            self.status = status

    @property
    def algorithm_image_version(self):
        r"""Gets the algorithm_image_version of this ListSimBatchesRequest.

        算法镜像版本

        :return: The algorithm_image_version of this ListSimBatchesRequest.
        :rtype: str
        """
        return self._algorithm_image_version

    @algorithm_image_version.setter
    def algorithm_image_version(self, algorithm_image_version):
        r"""Sets the algorithm_image_version of this ListSimBatchesRequest.

        算法镜像版本

        :param algorithm_image_version: The algorithm_image_version of this ListSimBatchesRequest.
        :type algorithm_image_version: str
        """
        self._algorithm_image_version = algorithm_image_version

    @property
    def algorithm_name(self):
        r"""Gets the algorithm_name of this ListSimBatchesRequest.

        算法名称

        :return: The algorithm_name of this ListSimBatchesRequest.
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        r"""Sets the algorithm_name of this ListSimBatchesRequest.

        算法名称

        :param algorithm_name: The algorithm_name of this ListSimBatchesRequest.
        :type algorithm_name: str
        """
        self._algorithm_name = algorithm_name

    @property
    def batch_config_id(self):
        r"""Gets the batch_config_id of this ListSimBatchesRequest.

        关联batch配置

        :return: The batch_config_id of this ListSimBatchesRequest.
        :rtype: int
        """
        return self._batch_config_id

    @batch_config_id.setter
    def batch_config_id(self, batch_config_id):
        r"""Sets the batch_config_id of this ListSimBatchesRequest.

        关联batch配置

        :param batch_config_id: The batch_config_id of this ListSimBatchesRequest.
        :type batch_config_id: int
        """
        self._batch_config_id = batch_config_id

    @property
    def description(self):
        r"""Gets the description of this ListSimBatchesRequest.

        描述

        :return: The description of this ListSimBatchesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListSimBatchesRequest.

        描述

        :param description: The description of this ListSimBatchesRequest.
        :type description: str
        """
        self._description = description

    @property
    def generalization_id(self):
        r"""Gets the generalization_id of this ListSimBatchesRequest.

        泛化任务id

        :return: The generalization_id of this ListSimBatchesRequest.
        :rtype: int
        """
        return self._generalization_id

    @generalization_id.setter
    def generalization_id(self, generalization_id):
        r"""Sets the generalization_id of this ListSimBatchesRequest.

        泛化任务id

        :param generalization_id: The generalization_id of this ListSimBatchesRequest.
        :type generalization_id: int
        """
        self._generalization_id = generalization_id

    @property
    def id(self):
        r"""Gets the id of this ListSimBatchesRequest.

        :return: The id of this ListSimBatchesRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSimBatchesRequest.

        :param id: The id of this ListSimBatchesRequest.
        :type id: int
        """
        self._id = id

    @property
    def limit(self):
        r"""Gets the limit of this ListSimBatchesRequest.

        Number of results to return per page.

        :return: The limit of this ListSimBatchesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimBatchesRequest.

        Number of results to return per page.

        :param limit: The limit of this ListSimBatchesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListSimBatchesRequest.

        :return: The name of this ListSimBatchesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSimBatchesRequest.

        :param name: The name of this ListSimBatchesRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListSimBatchesRequest.

        The initial index from which to return the results.

        :return: The offset of this ListSimBatchesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimBatchesRequest.

        The initial index from which to return the results.

        :param offset: The offset of this ListSimBatchesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def ordering(self):
        r"""Gets the ordering of this ListSimBatchesRequest.

        Which field to use when ordering the results.

        :return: The ordering of this ListSimBatchesRequest.
        :rtype: str
        """
        return self._ordering

    @ordering.setter
    def ordering(self, ordering):
        r"""Sets the ordering of this ListSimBatchesRequest.

        Which field to use when ordering the results.

        :param ordering: The ordering of this ListSimBatchesRequest.
        :type ordering: str
        """
        self._ordering = ordering

    @property
    def search(self):
        r"""Gets the search of this ListSimBatchesRequest.

        A search term.

        :return: The search of this ListSimBatchesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListSimBatchesRequest.

        A search term.

        :param search: The search of this ListSimBatchesRequest.
        :type search: str
        """
        self._search = search

    @property
    def status(self):
        r"""Gets the status of this ListSimBatchesRequest.

        任务状态

        :return: The status of this ListSimBatchesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSimBatchesRequest.

        任务状态

        :param status: The status of this ListSimBatchesRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ListSimBatchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
