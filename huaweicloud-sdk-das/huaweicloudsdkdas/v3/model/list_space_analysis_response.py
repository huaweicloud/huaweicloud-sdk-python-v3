# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpaceAnalysisResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'db_objects': 'list[DbObjectSpaceInfo]',
        'instance_info': 'InstanceSpaceInfo'
    }

    attribute_map = {
        'total': 'total',
        'db_objects': 'db_objects',
        'instance_info': 'instance_info'
    }

    def __init__(self, total=None, db_objects=None, instance_info=None):
        """ListSpaceAnalysisResponse

        The model defined in huaweicloud sdk

        :param total: 记录总数
        :type total: int
        :param db_objects: 数据库对象列表
        :type db_objects: list[:class:`huaweicloudsdkdas.v3.DbObjectSpaceInfo`]
        :param instance_info: 
        :type instance_info: :class:`huaweicloudsdkdas.v3.InstanceSpaceInfo`
        """
        
        super(ListSpaceAnalysisResponse, self).__init__()

        self._total = None
        self._db_objects = None
        self._instance_info = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if db_objects is not None:
            self.db_objects = db_objects
        if instance_info is not None:
            self.instance_info = instance_info

    @property
    def total(self):
        """Gets the total of this ListSpaceAnalysisResponse.

        记录总数

        :return: The total of this ListSpaceAnalysisResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSpaceAnalysisResponse.

        记录总数

        :param total: The total of this ListSpaceAnalysisResponse.
        :type total: int
        """
        self._total = total

    @property
    def db_objects(self):
        """Gets the db_objects of this ListSpaceAnalysisResponse.

        数据库对象列表

        :return: The db_objects of this ListSpaceAnalysisResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DbObjectSpaceInfo`]
        """
        return self._db_objects

    @db_objects.setter
    def db_objects(self, db_objects):
        """Sets the db_objects of this ListSpaceAnalysisResponse.

        数据库对象列表

        :param db_objects: The db_objects of this ListSpaceAnalysisResponse.
        :type db_objects: list[:class:`huaweicloudsdkdas.v3.DbObjectSpaceInfo`]
        """
        self._db_objects = db_objects

    @property
    def instance_info(self):
        """Gets the instance_info of this ListSpaceAnalysisResponse.

        :return: The instance_info of this ListSpaceAnalysisResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.InstanceSpaceInfo`
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        """Sets the instance_info of this ListSpaceAnalysisResponse.

        :param instance_info: The instance_info of this ListSpaceAnalysisResponse.
        :type instance_info: :class:`huaweicloudsdkdas.v3.InstanceSpaceInfo`
        """
        self._instance_info = instance_info

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
        if not isinstance(other, ListSpaceAnalysisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
