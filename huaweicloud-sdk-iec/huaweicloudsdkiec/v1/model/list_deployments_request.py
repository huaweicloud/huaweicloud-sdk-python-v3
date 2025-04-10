# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeploymentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'status': 'str',
        'id': 'str',
        'edgecloud_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'id': 'id',
        'edgecloud_id': 'edgecloud_id'
    }

    def __init__(self, offset=None, limit=None, status=None, id=None, edgecloud_id=None):
        r"""ListDeploymentsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量。 当前偏移量，默认为0。
        :type offset: int
        :param limit: 查询返回部署计划列表当前页面的数量。
        :type limit: int
        :param status: 查询条件，部署计划状态，现只包含如下值： - open:部署计划处于未执行状态，可执行部署计划进行部署 - closed:部署计划已关闭，不可部署。
        :type status: str
        :param id: 查询条件，部署计划ID。
        :type id: str
        :param edgecloud_id: 查询条件，边缘业务ID。
        :type edgecloud_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._status = None
        self._id = None
        self._edgecloud_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if edgecloud_id is not None:
            self.edgecloud_id = edgecloud_id

    @property
    def offset(self):
        r"""Gets the offset of this ListDeploymentsRequest.

        偏移量。 当前偏移量，默认为0。

        :return: The offset of this ListDeploymentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDeploymentsRequest.

        偏移量。 当前偏移量，默认为0。

        :param offset: The offset of this ListDeploymentsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDeploymentsRequest.

        查询返回部署计划列表当前页面的数量。

        :return: The limit of this ListDeploymentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDeploymentsRequest.

        查询返回部署计划列表当前页面的数量。

        :param limit: The limit of this ListDeploymentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListDeploymentsRequest.

        查询条件，部署计划状态，现只包含如下值： - open:部署计划处于未执行状态，可执行部署计划进行部署 - closed:部署计划已关闭，不可部署。

        :return: The status of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListDeploymentsRequest.

        查询条件，部署计划状态，现只包含如下值： - open:部署计划处于未执行状态，可执行部署计划进行部署 - closed:部署计划已关闭，不可部署。

        :param status: The status of this ListDeploymentsRequest.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        r"""Gets the id of this ListDeploymentsRequest.

        查询条件，部署计划ID。

        :return: The id of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListDeploymentsRequest.

        查询条件，部署计划ID。

        :param id: The id of this ListDeploymentsRequest.
        :type id: str
        """
        self._id = id

    @property
    def edgecloud_id(self):
        r"""Gets the edgecloud_id of this ListDeploymentsRequest.

        查询条件，边缘业务ID。

        :return: The edgecloud_id of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._edgecloud_id

    @edgecloud_id.setter
    def edgecloud_id(self, edgecloud_id):
        r"""Sets the edgecloud_id of this ListDeploymentsRequest.

        查询条件，边缘业务ID。

        :param edgecloud_id: The edgecloud_id of this ListDeploymentsRequest.
        :type edgecloud_id: str
        """
        self._edgecloud_id = edgecloud_id

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
        if not isinstance(other, ListDeploymentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
