# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddFacesByUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'face_set_name': 'str',
        'body': 'AddFacesUrlReq'
    }

    attribute_map = {
        'enterprise_project_id': 'Enterprise-Project-Id',
        'face_set_name': 'face_set_name',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, face_set_name=None, body=None):
        """AddFacesByUrlRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID。FRS支持通过企业项目管理（EPS）对不同用户组和用户的资源使用，进行分账。当前仅支持按需计费模式。  获取方法：进入“[企业项目管理](https://console.huaweicloud.com/eps/?region&#x3D;cn-north-4#/projects/list)”页面，单击企业项目名称，在企业项目详情页获取Enterprise-Project-Id（企业项目ID）。  企业项目创建步骤请参见用户指南。 &gt; 说明： 创建企业项目后，在传参时，有以下三类场景。 - 携带正确的ID，正常使用FRS服务，账单归到企业ID对应的企业项目中。 - 携带错误的ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。 - 不携带ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。
        :type enterprise_project_id: str
        :param face_set_name: 人脸库名称。
        :type face_set_name: str
        :param body: Body of the AddFacesByUrlRequest
        :type body: :class:`huaweicloudsdkfrs.v2.AddFacesUrlReq`
        """
        
        

        self._enterprise_project_id = None
        self._face_set_name = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.face_set_name = face_set_name
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this AddFacesByUrlRequest.

        企业项目ID。FRS支持通过企业项目管理（EPS）对不同用户组和用户的资源使用，进行分账。当前仅支持按需计费模式。  获取方法：进入“[企业项目管理](https://console.huaweicloud.com/eps/?region=cn-north-4#/projects/list)”页面，单击企业项目名称，在企业项目详情页获取Enterprise-Project-Id（企业项目ID）。  企业项目创建步骤请参见用户指南。 > 说明： 创建企业项目后，在传参时，有以下三类场景。 - 携带正确的ID，正常使用FRS服务，账单归到企业ID对应的企业项目中。 - 携带错误的ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。 - 不携带ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。

        :return: The enterprise_project_id of this AddFacesByUrlRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this AddFacesByUrlRequest.

        企业项目ID。FRS支持通过企业项目管理（EPS）对不同用户组和用户的资源使用，进行分账。当前仅支持按需计费模式。  获取方法：进入“[企业项目管理](https://console.huaweicloud.com/eps/?region=cn-north-4#/projects/list)”页面，单击企业项目名称，在企业项目详情页获取Enterprise-Project-Id（企业项目ID）。  企业项目创建步骤请参见用户指南。 > 说明： 创建企业项目后，在传参时，有以下三类场景。 - 携带正确的ID，正常使用FRS服务，账单归到企业ID对应的企业项目中。 - 携带错误的ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。 - 不携带ID，正常使用FRS服务，账单的企业项目会被分类为“未归集”。

        :param enterprise_project_id: The enterprise_project_id of this AddFacesByUrlRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def face_set_name(self):
        """Gets the face_set_name of this AddFacesByUrlRequest.

        人脸库名称。

        :return: The face_set_name of this AddFacesByUrlRequest.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        """Sets the face_set_name of this AddFacesByUrlRequest.

        人脸库名称。

        :param face_set_name: The face_set_name of this AddFacesByUrlRequest.
        :type face_set_name: str
        """
        self._face_set_name = face_set_name

    @property
    def body(self):
        """Gets the body of this AddFacesByUrlRequest.

        :return: The body of this AddFacesByUrlRequest.
        :rtype: :class:`huaweicloudsdkfrs.v2.AddFacesUrlReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AddFacesByUrlRequest.

        :param body: The body of this AddFacesByUrlRequest.
        :type body: :class:`huaweicloudsdkfrs.v2.AddFacesUrlReq`
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
        if not isinstance(other, AddFacesByUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
