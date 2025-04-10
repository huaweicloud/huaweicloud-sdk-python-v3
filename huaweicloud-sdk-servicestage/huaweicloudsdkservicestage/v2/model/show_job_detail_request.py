# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'instance_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'desc': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'desc': 'desc'
    }

    def __init__(self, job_id=None, instance_id=None, limit=None, offset=None, desc=None):
        r"""ShowJobDetailRequest

        The model defined in huaweicloud sdk

        :param job_id: 部署任务ID。
        :type job_id: str
        :param instance_id: 应用组件实例ID。
        :type instance_id: str
        :param limit: 指定查询的个数，可用于分页查询。
        :type limit: int
        :param offset: 指定查询的偏移量，可用于分页查询。
        :type offset: int
        :param desc: 是否降序。true表示desc, false表示asc。
        :type desc: str
        """
        
        

        self._job_id = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self._desc = None
        self.discriminator = None

        self.job_id = job_id
        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if desc is not None:
            self.desc = desc

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowJobDetailRequest.

        部署任务ID。

        :return: The job_id of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowJobDetailRequest.

        部署任务ID。

        :param job_id: The job_id of this ShowJobDetailRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowJobDetailRequest.

        应用组件实例ID。

        :return: The instance_id of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowJobDetailRequest.

        应用组件实例ID。

        :param instance_id: The instance_id of this ShowJobDetailRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowJobDetailRequest.

        指定查询的个数，可用于分页查询。

        :return: The limit of this ShowJobDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowJobDetailRequest.

        指定查询的个数，可用于分页查询。

        :param limit: The limit of this ShowJobDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowJobDetailRequest.

        指定查询的偏移量，可用于分页查询。

        :return: The offset of this ShowJobDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowJobDetailRequest.

        指定查询的偏移量，可用于分页查询。

        :param offset: The offset of this ShowJobDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def desc(self):
        r"""Gets the desc of this ShowJobDetailRequest.

        是否降序。true表示desc, false表示asc。

        :return: The desc of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ShowJobDetailRequest.

        是否降序。true表示desc, false表示asc。

        :param desc: The desc of this ShowJobDetailRequest.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, ShowJobDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
