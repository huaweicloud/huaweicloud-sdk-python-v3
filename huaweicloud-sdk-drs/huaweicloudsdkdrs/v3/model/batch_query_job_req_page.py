# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchQueryJobReqPage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'jobs': 'list[str]',
        'page_req': 'PageReq'
    }

    attribute_map = {
        'jobs': 'jobs',
        'page_req': 'page_req'
    }

    def __init__(self, jobs=None, page_req=None):
        """BatchQueryJobReqPage

        The model defined in huaweicloud sdk

        :param jobs: 批量查询任务详情
        :type jobs: list[str]
        :param page_req: 
        :type page_req: :class:`huaweicloudsdkdrs.v3.PageReq`
        """
        
        

        self._jobs = None
        self._page_req = None
        self.discriminator = None

        self.jobs = jobs
        if page_req is not None:
            self.page_req = page_req

    @property
    def jobs(self):
        """Gets the jobs of this BatchQueryJobReqPage.

        批量查询任务详情

        :return: The jobs of this BatchQueryJobReqPage.
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this BatchQueryJobReqPage.

        批量查询任务详情

        :param jobs: The jobs of this BatchQueryJobReqPage.
        :type jobs: list[str]
        """
        self._jobs = jobs

    @property
    def page_req(self):
        """Gets the page_req of this BatchQueryJobReqPage.


        :return: The page_req of this BatchQueryJobReqPage.
        :rtype: :class:`huaweicloudsdkdrs.v3.PageReq`
        """
        return self._page_req

    @page_req.setter
    def page_req(self, page_req):
        """Sets the page_req of this BatchQueryJobReqPage.


        :param page_req: The page_req of this BatchQueryJobReqPage.
        :type page_req: :class:`huaweicloudsdkdrs.v3.PageReq`
        """
        self._page_req = page_req

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
        if not isinstance(other, BatchQueryJobReqPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
