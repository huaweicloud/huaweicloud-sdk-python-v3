# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobEndpointsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ssh': 'SSHResp',
        'jupyter_lab': 'JupyterLab',
        'tensorboard': 'Tensorboard',
        'mindstudio_insight': 'MindStudioInsight'
    }

    attribute_map = {
        'ssh': 'ssh',
        'jupyter_lab': 'jupyter_lab',
        'tensorboard': 'tensorboard',
        'mindstudio_insight': 'mindstudio_insight'
    }

    def __init__(self, ssh=None, jupyter_lab=None, tensorboard=None, mindstudio_insight=None):
        r"""JobEndpointsResp

        The model defined in huaweicloud sdk

        :param ssh: 
        :type ssh: :class:`huaweicloudsdkmodelarts.v1.SSHResp`
        :param jupyter_lab: 
        :type jupyter_lab: :class:`huaweicloudsdkmodelarts.v1.JupyterLab`
        :param tensorboard: 
        :type tensorboard: :class:`huaweicloudsdkmodelarts.v1.Tensorboard`
        :param mindstudio_insight: 
        :type mindstudio_insight: :class:`huaweicloudsdkmodelarts.v1.MindStudioInsight`
        """
        
        

        self._ssh = None
        self._jupyter_lab = None
        self._tensorboard = None
        self._mindstudio_insight = None
        self.discriminator = None

        if ssh is not None:
            self.ssh = ssh
        if jupyter_lab is not None:
            self.jupyter_lab = jupyter_lab
        if tensorboard is not None:
            self.tensorboard = tensorboard
        if mindstudio_insight is not None:
            self.mindstudio_insight = mindstudio_insight

    @property
    def ssh(self):
        r"""Gets the ssh of this JobEndpointsResp.

        :return: The ssh of this JobEndpointsResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SSHResp`
        """
        return self._ssh

    @ssh.setter
    def ssh(self, ssh):
        r"""Sets the ssh of this JobEndpointsResp.

        :param ssh: The ssh of this JobEndpointsResp.
        :type ssh: :class:`huaweicloudsdkmodelarts.v1.SSHResp`
        """
        self._ssh = ssh

    @property
    def jupyter_lab(self):
        r"""Gets the jupyter_lab of this JobEndpointsResp.

        :return: The jupyter_lab of this JobEndpointsResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JupyterLab`
        """
        return self._jupyter_lab

    @jupyter_lab.setter
    def jupyter_lab(self, jupyter_lab):
        r"""Sets the jupyter_lab of this JobEndpointsResp.

        :param jupyter_lab: The jupyter_lab of this JobEndpointsResp.
        :type jupyter_lab: :class:`huaweicloudsdkmodelarts.v1.JupyterLab`
        """
        self._jupyter_lab = jupyter_lab

    @property
    def tensorboard(self):
        r"""Gets the tensorboard of this JobEndpointsResp.

        :return: The tensorboard of this JobEndpointsResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Tensorboard`
        """
        return self._tensorboard

    @tensorboard.setter
    def tensorboard(self, tensorboard):
        r"""Sets the tensorboard of this JobEndpointsResp.

        :param tensorboard: The tensorboard of this JobEndpointsResp.
        :type tensorboard: :class:`huaweicloudsdkmodelarts.v1.Tensorboard`
        """
        self._tensorboard = tensorboard

    @property
    def mindstudio_insight(self):
        r"""Gets the mindstudio_insight of this JobEndpointsResp.

        :return: The mindstudio_insight of this JobEndpointsResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.MindStudioInsight`
        """
        return self._mindstudio_insight

    @mindstudio_insight.setter
    def mindstudio_insight(self, mindstudio_insight):
        r"""Sets the mindstudio_insight of this JobEndpointsResp.

        :param mindstudio_insight: The mindstudio_insight of this JobEndpointsResp.
        :type mindstudio_insight: :class:`huaweicloudsdkmodelarts.v1.MindStudioInsight`
        """
        self._mindstudio_insight = mindstudio_insight

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobEndpointsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
