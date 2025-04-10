# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCancelJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_force': 'bool',
        'eihealth_project_id': 'str',
        'body': 'BatchOperateJobReq'
    }

    attribute_map = {
        'x_force': 'X-Force',
        'eihealth_project_id': 'eihealth_project_id',
        'body': 'body'
    }

    def __init__(self, x_force=None, eihealth_project_id=None, body=None):
        r"""BatchCancelJobRequest

        The model defined in huaweicloud sdk

        :param x_force: 是否强制停止作业
        :type x_force: bool
        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param body: Body of the BatchCancelJobRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.BatchOperateJobReq`
        """
        
        

        self._x_force = None
        self._eihealth_project_id = None
        self._body = None
        self.discriminator = None

        if x_force is not None:
            self.x_force = x_force
        self.eihealth_project_id = eihealth_project_id
        if body is not None:
            self.body = body

    @property
    def x_force(self):
        r"""Gets the x_force of this BatchCancelJobRequest.

        是否强制停止作业

        :return: The x_force of this BatchCancelJobRequest.
        :rtype: bool
        """
        return self._x_force

    @x_force.setter
    def x_force(self, x_force):
        r"""Sets the x_force of this BatchCancelJobRequest.

        是否强制停止作业

        :param x_force: The x_force of this BatchCancelJobRequest.
        :type x_force: bool
        """
        self._x_force = x_force

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this BatchCancelJobRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this BatchCancelJobRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this BatchCancelJobRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this BatchCancelJobRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def body(self):
        r"""Gets the body of this BatchCancelJobRequest.

        :return: The body of this BatchCancelJobRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchOperateJobReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCancelJobRequest.

        :param body: The body of this BatchCancelJobRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.BatchOperateJobReq`
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
        if not isinstance(other, BatchCancelJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
