# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIndicatorsRequest:

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
        'workspace_id': 'str',
        'order': 'str',
        'from_date': 'str',
        'to_date': 'str',
        'body': 'IndicatorListSearchRequest'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'order': 'order',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, order=None, from_date=None, to_date=None, body=None):
        """ListIndicatorsRequest

        The model defined in huaweicloud sdk

        :param project_id: ID of project
        :type project_id: str
        :param workspace_id: workspace id
        :type workspace_id: str
        :param order: sort order, ASC, DESC.
        :type order: str
        :param from_date: 起始时间
        :type from_date: str
        :param to_date: 结束时间
        :type to_date: str
        :param body: Body of the ListIndicatorsRequest
        :type body: :class:`huaweicloudsdksa.v2.IndicatorListSearchRequest`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._order = None
        self._from_date = None
        self._to_date = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if order is not None:
            self.order = order
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        """Gets the project_id of this ListIndicatorsRequest.

        ID of project

        :return: The project_id of this ListIndicatorsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListIndicatorsRequest.

        ID of project

        :param project_id: The project_id of this ListIndicatorsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListIndicatorsRequest.

        workspace id

        :return: The workspace_id of this ListIndicatorsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListIndicatorsRequest.

        workspace id

        :param workspace_id: The workspace_id of this ListIndicatorsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def order(self):
        """Gets the order of this ListIndicatorsRequest.

        sort order, ASC, DESC.

        :return: The order of this ListIndicatorsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListIndicatorsRequest.

        sort order, ASC, DESC.

        :param order: The order of this ListIndicatorsRequest.
        :type order: str
        """
        self._order = order

    @property
    def from_date(self):
        """Gets the from_date of this ListIndicatorsRequest.

        起始时间

        :return: The from_date of this ListIndicatorsRequest.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this ListIndicatorsRequest.

        起始时间

        :param from_date: The from_date of this ListIndicatorsRequest.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this ListIndicatorsRequest.

        结束时间

        :return: The to_date of this ListIndicatorsRequest.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this ListIndicatorsRequest.

        结束时间

        :param to_date: The to_date of this ListIndicatorsRequest.
        :type to_date: str
        """
        self._to_date = to_date

    @property
    def body(self):
        """Gets the body of this ListIndicatorsRequest.

        :return: The body of this ListIndicatorsRequest.
        :rtype: :class:`huaweicloudsdksa.v2.IndicatorListSearchRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListIndicatorsRequest.

        :param body: The body of this ListIndicatorsRequest.
        :type body: :class:`huaweicloudsdksa.v2.IndicatorListSearchRequest`
        """
        self._body = body

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
        if not isinstance(other, ListIndicatorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
