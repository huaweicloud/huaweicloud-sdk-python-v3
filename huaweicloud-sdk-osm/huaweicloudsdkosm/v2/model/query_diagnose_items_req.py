# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDiagnoseItemsReq:

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
        'item_ids': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'item_ids': 'item_ids'
    }

    def __init__(self, job_id=None, item_ids=None):
        """QueryDiagnoseItemsReq

        The model defined in huaweicloud sdk

        :param job_id: job id
        :type job_id: str
        :param item_ids: 诊断项id列表
        :type item_ids: str
        """
        
        

        self._job_id = None
        self._item_ids = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if item_ids is not None:
            self.item_ids = item_ids

    @property
    def job_id(self):
        """Gets the job_id of this QueryDiagnoseItemsReq.

        job id

        :return: The job_id of this QueryDiagnoseItemsReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this QueryDiagnoseItemsReq.

        job id

        :param job_id: The job_id of this QueryDiagnoseItemsReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def item_ids(self):
        """Gets the item_ids of this QueryDiagnoseItemsReq.

        诊断项id列表

        :return: The item_ids of this QueryDiagnoseItemsReq.
        :rtype: str
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        """Sets the item_ids of this QueryDiagnoseItemsReq.

        诊断项id列表

        :param item_ids: The item_ids of this QueryDiagnoseItemsReq.
        :type item_ids: str
        """
        self._item_ids = item_ids

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
        if not isinstance(other, QueryDiagnoseItemsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
