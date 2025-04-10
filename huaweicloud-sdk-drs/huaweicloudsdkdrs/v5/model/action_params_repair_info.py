# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionParamsRepairInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_id': 'str',
        'objects': 'list[ActionParamsRepairInfoObjects]'
    }

    attribute_map = {
        'query_id': 'query_id',
        'objects': 'objects'
    }

    def __init__(self, query_id=None, objects=None):
        r"""ActionParamsRepairInfo

        The model defined in huaweicloud sdk

        :param query_id: 对比任务ID。
        :type query_id: str
        :param objects: 数据修复对象信息。
        :type objects: list[:class:`huaweicloudsdkdrs.v5.ActionParamsRepairInfoObjects`]
        """
        
        

        self._query_id = None
        self._objects = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if objects is not None:
            self.objects = objects

    @property
    def query_id(self):
        r"""Gets the query_id of this ActionParamsRepairInfo.

        对比任务ID。

        :return: The query_id of this ActionParamsRepairInfo.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this ActionParamsRepairInfo.

        对比任务ID。

        :param query_id: The query_id of this ActionParamsRepairInfo.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def objects(self):
        r"""Gets the objects of this ActionParamsRepairInfo.

        数据修复对象信息。

        :return: The objects of this ActionParamsRepairInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ActionParamsRepairInfoObjects`]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        r"""Sets the objects of this ActionParamsRepairInfo.

        数据修复对象信息。

        :param objects: The objects of this ActionParamsRepairInfo.
        :type objects: list[:class:`huaweicloudsdkdrs.v5.ActionParamsRepairInfoObjects`]
        """
        self._objects = objects

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
        if not isinstance(other, ActionParamsRepairInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
