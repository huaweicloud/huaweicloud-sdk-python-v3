# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectIterationsV4Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'updated_time_interval': 'str',
        'include_deleted': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'updated_time_interval': 'updated_time_interval',
        'include_deleted': 'include_deleted'
    }

    def __init__(self, project_id=None, updated_time_interval=None, include_deleted=None):
        """ListProjectIterationsV4Request

        The model defined in huaweicloud sdk

        :param project_id: devcloud项目的32位id
        :type project_id: str
        :param updated_time_interval: 更新迭代的时间(查询的起始时间,查询的结束时间)
        :type updated_time_interval: str
        :param include_deleted: 是否包含被删除的迭代,默认false不包含被删除的迭代
        :type include_deleted: bool
        """
        
        

        self._project_id = None
        self._updated_time_interval = None
        self._include_deleted = None
        self.discriminator = None

        self.project_id = project_id
        if updated_time_interval is not None:
            self.updated_time_interval = updated_time_interval
        if include_deleted is not None:
            self.include_deleted = include_deleted

    @property
    def project_id(self):
        """Gets the project_id of this ListProjectIterationsV4Request.

        devcloud项目的32位id

        :return: The project_id of this ListProjectIterationsV4Request.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListProjectIterationsV4Request.

        devcloud项目的32位id

        :param project_id: The project_id of this ListProjectIterationsV4Request.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def updated_time_interval(self):
        """Gets the updated_time_interval of this ListProjectIterationsV4Request.

        更新迭代的时间(查询的起始时间,查询的结束时间)

        :return: The updated_time_interval of this ListProjectIterationsV4Request.
        :rtype: str
        """
        return self._updated_time_interval

    @updated_time_interval.setter
    def updated_time_interval(self, updated_time_interval):
        """Sets the updated_time_interval of this ListProjectIterationsV4Request.

        更新迭代的时间(查询的起始时间,查询的结束时间)

        :param updated_time_interval: The updated_time_interval of this ListProjectIterationsV4Request.
        :type updated_time_interval: str
        """
        self._updated_time_interval = updated_time_interval

    @property
    def include_deleted(self):
        """Gets the include_deleted of this ListProjectIterationsV4Request.

        是否包含被删除的迭代,默认false不包含被删除的迭代

        :return: The include_deleted of this ListProjectIterationsV4Request.
        :rtype: bool
        """
        return self._include_deleted

    @include_deleted.setter
    def include_deleted(self, include_deleted):
        """Sets the include_deleted of this ListProjectIterationsV4Request.

        是否包含被删除的迭代,默认false不包含被删除的迭代

        :param include_deleted: The include_deleted of this ListProjectIterationsV4Request.
        :type include_deleted: bool
        """
        self._include_deleted = include_deleted

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
        if not isinstance(other, ListProjectIterationsV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
