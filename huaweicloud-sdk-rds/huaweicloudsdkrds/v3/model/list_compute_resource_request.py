# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListComputeResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'engine': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'engine': 'engine'
    }

    def __init__(self, limit=None, offset=None, engine=None):
        r"""ListComputeResourceRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询，大小，默认为10
        :type limit: int
        :param offset: 分页查询，偏移量，默认为0
        :type offset: int
        :param engine: 引擎名称： mysql、sqlserver、postgresql
        :type engine: str
        """
        
        

        self._limit = None
        self._offset = None
        self._engine = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if engine is not None:
            self.engine = engine

    @property
    def limit(self):
        r"""Gets the limit of this ListComputeResourceRequest.

        分页查询，大小，默认为10

        :return: The limit of this ListComputeResourceRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListComputeResourceRequest.

        分页查询，大小，默认为10

        :param limit: The limit of this ListComputeResourceRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListComputeResourceRequest.

        分页查询，偏移量，默认为0

        :return: The offset of this ListComputeResourceRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListComputeResourceRequest.

        分页查询，偏移量，默认为0

        :param offset: The offset of this ListComputeResourceRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def engine(self):
        r"""Gets the engine of this ListComputeResourceRequest.

        引擎名称： mysql、sqlserver、postgresql

        :return: The engine of this ListComputeResourceRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListComputeResourceRequest.

        引擎名称： mysql、sqlserver、postgresql

        :param engine: The engine of this ListComputeResourceRequest.
        :type engine: str
        """
        self._engine = engine

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListComputeResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
